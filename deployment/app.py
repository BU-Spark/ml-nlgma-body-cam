import whisper
import cv2
import os
import urllib.request
from PIL import Image
from ultralytics import YOLO
import torch
import matplotlib.pyplot as plt
from tqdm import tqdm
from transformers import pipeline
import moviepy.editor as mp
import json
import re
import gradio as gr
from openai import OpenAI

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate
from langchain.schema.messages import SystemMessage
from langchain.prompts import ChatPromptTemplate

def video_transcription(video_path):
    model = whisper.load_model('large')
    transcript = model.transcribe(video_path, verbose = True, language = 'en')
    print(transcript)

    return json.dumps(transcript)

def action_detection(json_object, openai_key):
    transcript = json.loads(json_object)
    transcript_string = ''
    for segments in transcript['segments']:
      transcript_string+=str(segments['text']+'\n')

    chunks = []
    output = {}
    count = 0
    split_transcript = transcript_string.split("\n")
    num_lines = len(split_transcript)
    num_chars = 0
    i = 0
    prev = 0

    while i < num_lines:
      num_chars+=len(split_transcript[i])
      if num_chars>=16000:
        chunks.append("\n".join(split_transcript[prev:i]))
        prev = i
        num_chars = 0
      i+=1
      if i == num_lines:
        chunks.append("\n".join(split_transcript[prev:i]))

    # client = OpenAI(api_key = openai_key)
    llm = OpenAI(openai_api_key=openai_key, model="gpt-4")
    chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                "You are an AI system specialized in detecting planning issues, critiquing plans, and analyzing conversations between police officers regarding how to disperse." 
                "Additionally, identify any instances suggesting 1st Amendment violations, criticizing the lack of a plan, and aggressive comments. Transcript:\n\n{transcript_}\n\n." 
                "Give response only in the json format for example: \{\"1\":  \"What should we do now. I don't have a clue?\", \"2\": \"what the fuck is this\", \"3\":\"Beat the fuck out of them\"\}."
                "There can be multiple instances, find out all of them. If you do not find anything just return {\"None\":\"None\"}"
            )
        ),
        HumanMessagePromptTemplate.from_template("{transcript_}"),
    ]
)


    for i in chunks:
      prompt = PromptTemplate.from_template(
    "You are an AI system specialized in detecting planning issues, critiquing plans, and analyzing conversations between police officers regarding how to disperse. Additionally, identify any instances suggesting 1st Amendment violations, criticizing the lack of a plan, and aggressive comments. Transcript:\n\n{i}\n\n. Give response only in the json format for example: \{\"1\":  \"What should we do now. I don't have a clue?\", \"2\": \"what the fuck is this\", \"3\":\"Beat the fuck out of them\"\}. There can be multiple instances, find out all of them. If you do not find anything just return {\"None\":\"None\"}"
    )
      
      llm = ChatOpenAI(openai_api_key=openai_key)
      p = chat_template.format_messages(transcript_=i)
      gpt_output = llm(p).content
   
    #   print(gpt_output)
      # gpt_output = completion.choices[0].message.content
    #   print(gpt_output)
      
      
      
      
      gpt_output = dict(json.loads(gpt_output))
      for j in gpt_output.values():
       output[count] = j
       count+=1

    sent_with_time = []

    for sentence_to_search in output.values():
        pattern = re.compile(re.escape(sentence_to_search), re.IGNORECASE)

        matching_entries = [entry for entry in transcript['segments'] if re.search(pattern, entry['text'])]

        if matching_entries:
            for entry in matching_entries:
                hours_s, remainder = divmod(entry['start'], 3600)
                minutes_s, seconds_s = divmod(remainder, 60)
                hours_s = str(int(hours_s)).zfill(2)
                minutes_s = str(int(minutes_s)).zfill(2)
                seconds_s = str(int(seconds_s)).zfill(2)

                
                hours_e, remainder = divmod(entry['end'], 3600)
                minutes_e, seconds_e = divmod(remainder, 60)
                hours_e = str(int(hours_e)).zfill(2)
                minutes_e = str(int(minutes_e)).zfill(2)
                seconds_e = str(int(seconds_e)).zfill(2)

                sent_with_time.append(sentence_to_search + ' Start Time: ' + str(hours_s) + ":" + str(minutes_s) + ":" + str(seconds_s) + ' End Time: ' + str(hours_e) + ":" + str(minutes_e) + ":" + str(seconds_e))

    return "\n".join(sent_with_time)

def process_video(video_path, weights):
    try:
        # This code cell detects batons in the video
        current_frame = 0
        model = YOLO(weights)
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        conseq_frames = 0
        start_time = ""
        end_time = ""
        res = []

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Detecting baton on one frame per second
            if current_frame % fps == 0:
                currect_sec = current_frame/fps

                # Model prediction on current frame
                results = model(frame, verbose = False)
                count = 0
                classes = results[0].boxes.data

                # Formatting the time for printing
                hours, remainder = divmod(currect_sec, 3600)
                minutes, seconds = divmod(remainder, 60)
                hours = str(int(hours)).zfill(2)
                minutes = str(int(minutes)).zfill(2)
                seconds = str(int(seconds)).zfill(2)

                for i in classes:

                   # Checking if baton is detected (i.e. if the class corresponding to baton is 1 or not)
                    if float(i[5]) == 1:
                        count+=1

                # Marking the start_time if this is the first consecutive frame a baton is detected in
                if count >= 1:
                    conseq_frames+=1
                    if conseq_frames == 1:
                        start_time = hours + ":" + minutes + ":" + seconds

                # Marking the end time if after one or multiple consecutive frames of detection, a baton is not detected
                else:
                    if conseq_frames > 0:
                        conseq_frames = 0
                        end_time = hours + ":" + minutes + ":" + seconds

                        # Printing time intervals in which baton was detected
                        res.append(start_time + " to " + end_time)
                        start_time = ""
                        end_time = ""

            current_frame += 1
        cap.release()

        return "\n".join(res)

    except Exception as e:

        return e

def all_funcs(openai_key,video_path, yolo_weights, pr = gr.Progress(track_tqdm = True)):

  
  video_path = video_path[0].split('/')[-1]
  yolo_weights = yolo_weights[0].split('/')[-1]
  transcript = video_transcription(video_path)
  sentences = action_detection(transcript, openai_key)
  batons = process_video(video_path, yolo_weights)

  print("ALL FUNC Executed without errors")

  return sentences, batons


btn = gr.Interface(
    fn = all_funcs,
    inputs = ["text", gr.Files(label = "Select Video File"), gr.Files(label = "Select YOLOv8 Weights File")],
    outputs=[gr.Textbox(label = "Audio Analysis Time Stamps", lines = 20), gr.Textbox(label = "Baton Detection Timestamps", lines = 20)]
)

btn.launch(server_name="0.0.0.0")