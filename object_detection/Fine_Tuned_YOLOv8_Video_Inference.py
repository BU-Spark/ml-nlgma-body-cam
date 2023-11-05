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
device = "cuda" if torch.cuda.is_available() else "cpu"

cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))

while True:
    ret, frame = cap.read()
    if not ret:
      break

    if current_frame % fps == 0:
      currect_sec = current_frame/fps
      results = model(frame, verbose = False)
      count = 0
      classes = results[0].boxes.data
      for i in classes:
        if float(i[5]) == 1:
          count+=1
      if count >= 1:
        hours, remainder = divmod(currect_sec, 3600)
        minutes, seconds = divmod(remainder, 60)
        hours = str(int(hours)).zfill(2)
        minutes = str(int(minutes)).zfill(2)
        seconds = str(int(seconds)).zfill(2)
        print(f"Baton found at {hours}:{minutes}:{seconds}")

    current_frame += 1

cap.release()