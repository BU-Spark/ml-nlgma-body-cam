import cv2
import os
from PIL import Image
import torch
from transformers import OwlViTProcessor, OwlViTForObjectDetection
import matplotlib.pyplot as plt
from tqdm import tqdm

def plot_predictions(input_image, text_queries, boxes, scores, labels, threshold = 0.03):
  fig, ax = plt.subplots(1, 1, figsize=(8, 8))
  ax.imshow(input_image, extent=(0, 1, 1, 0))
  ax.set_axis_off()

  for score, box, label in zip(scores, boxes, labels):
    if score < threshold:
      continue

    cx, cy, w, h = box
    ax.plot([cx-w/2, cx+w/2, cx+w/2, cx-w/2, cx-w/2], [cy-h/2, cy-h/2, cy+h/2, cy+h/2, cy-h/2], "r")
    ax.text(cx-w/2, cy+h/2+0.015, f"{text_queries[label]}: {score:1.2f}", ha = "left", va = "top", color = "red",
            bbox={
            "facecolor": "white",
            "edgecolor": "red",
            "boxstyle": "square, pad = .3"
        })

video_path = ""
model_folder = ""
threshold = 0.03
current_frame = 0

device = "cuda" if torch.cuda.is_available() else "cpu"
processor = OwlViTProcessor.from_pretrained(model_folder)
model = OwlViTForObjectDetection.from_pretrained(model_folder)
model = model.to(device)

cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))

while True:
    ret, frame = cap.read()
    if not ret:
      break

    #current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000
    #if current_time >= end_seconds:
    #  break

    if current_frame % fps == 0:
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      image = Image.fromarray(frame)
      texts = [["a stick"]]
      inputs = processor(text = texts, images = image, return_tensors = "pt")
      inputs = {k: v.to(device) for k, v in inputs.items()}

      outputs = model(**inputs)
      target_sizes = torch.Tensor([image.size[::-1]]).to(device)
      results = processor.post_process_object_detection(outputs = outputs, threshold = 0.1, target_sizes = target_sizes)

      logits = torch.max(outputs["logits"][0], dim = -1)
      scores = torch.sigmoid(logits.values).cpu().detach().numpy()
      labels = logits.indices.cpu().detach().numpy()
      boxes = outputs["pred_boxes"][0].cpu().detach().numpy()

      plot_predictions(image, texts, boxes, scores, labels, threshold)

    current_frame += 1

cap.release()