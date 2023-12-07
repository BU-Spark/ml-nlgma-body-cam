## BPD BodyCam Timestamps

Legal cases arise in which police body camera footage may be a source of important evidence. A critical aspect of these cases involves analyzing body camera footage, which can vary greatly in length from minutes to hours. The current manual review process is time-consuming and labor-intensive. The aim of this project is to use AI to find moments where:

1. Officers complain about the lack of a plan
2. Officers fail to offer people with directions
3. Officers direct aggressive comments at protestors

The project aims to develop an automated system for the analysis of body camera footage. This system will utilize advanced Automatic Speech Recognition (ASR) and Natural Language Processing (NLP) techniques to identify and extract specific actions and events from the videos. These ASR and NLP models could be programmed to recognize instances of aggressive comments and lack of a plan. Additionally, the system could generate searchable metadata associated with each video clip.

Checklist:
- Train/Implement ASR model(s) to extract a transcript of the audio in all videos
- Train/Implement NLP model(s) on the extracted text.
- Identify and timestamp specific events (e.g., lack of planning, aggressive comments, and failure to provide directions to protestors) from the videos.

Deployment colab:
<a target="_blank" href="https://colab.research.google.com/github/k-sashank/ml-nlgma-body-cam/blob/main/deployment/Spark_Deployment.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
