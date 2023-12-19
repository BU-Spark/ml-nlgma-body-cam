## BPD BodyCam Timestamps

The Law Offices of Howard Friedman specializes in civil lawsuits representing victims of police brutality, false arrest, wrongful death, and civil rights violations. A critical aspect of these cases involves analyzing body camera footage, which can vary greatly in length from minutes to hours. The current manual review process is time-consuming and labor-intensive. The aim of this project is to use AI to find moments where:

1. Officers complain about the lack of a plan
2. Officers fail to offer people with directions
3. Officers direct aggressive comments at protestors
4. Officers using batons forcefully towards the protestors

The project aims to develop an automated system for the analysis of body camera footage. This system will utilize advanced Automatic Speech Recognition (ASR) and Natural Language Processing (NLP) techniques to identify and extract specific actions and events from the videos. These ASR and NLP models could be programmed to recognize instances of aggressive comments and lack of a plan. Additionally, the system could generate searchable metadata associated with each video clip.

Deployment colab:
<a target="_blank" href="https://colab.research.google.com/github/k-sashank/ml-nlgma-body-cam/blob/main/deployment/Spark_Deployment_Final.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

The final application works as follows:
1. The application needs three entities i.e. the YOLOv8 pre-trained weights, the video file to be analyzed, and the OpenAI key.
2. Once these three entities are supplied, the application runs the three models i.e. Whisper followed by GPT-4 and YOLOv8.
3. After processing, the application displays the timestamps of the dialogues (pertaining to the first three incidents) as well as the timestamps of the batons.

The Docker Image for this project is publicly available at:
aakash0017/ml-nlgma-body-cam/

Instructions on running the application from a docker image can be found here:
https://docs.docker.com/engine/reference/commandline/run/

The pre-trained weights for the YOLOv8 model can be found and downloaded here:
https://drive.google.com/file/d/1IlKpRO27gYErr4NZvhfuTwyliRgKvc8m/view?usp=sharing

The final project presentation has also been added to the repo. This will give the required background to understand the project and the repo.
