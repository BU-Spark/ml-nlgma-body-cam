import cv2
import os
import urllib.request
from PIL import Image
from ultralytics import YOLO
import torch
import matplotlib.pyplot as plt
from tqdm import tqdm

# Add path to YOLOv8 Fine-Tuned Model Weights
model = YOLO("")

# Add path to video
video_path = ""

current_frame = 0

cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
conseq_frames = 0
start_time = ""
end_time = ""

while True:
    ret, frame = cap.read()
    if not ret:
      break

    if current_frame % fps == 0:
      currect_sec = current_frame/fps
      results = model(frame, verbose = False)
      count = 0
      classes = results[0].boxes.data

      hours, remainder = divmod(currect_sec, 3600)
      minutes, seconds = divmod(remainder, 60)
      hours = str(int(hours)).zfill(2)
      minutes = str(int(minutes)).zfill(2)
      seconds = str(int(seconds)).zfill(2)
      
      for i in classes:
        if float(i[5]) == 1:
          count+=1
      if count >= 1:
        conseq_frames+=1
        if conseq_frames == 1:
          start_time = hours + ":" + minutes + ":" + seconds
      else:
        if conseq_frames > 0:
          conseq_frames = 0
          end_time = hours + ":" + minutes + ":" + seconds
          print(f"Baton found from {start_time} to {end_time}")
          start_time = ""
          end_time = ""

    current_frame += 1

cap.release()