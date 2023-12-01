FROM python:3.10.9

WORKDIR /workspace

RUN cd /workspace
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

COPY . .


# ADD requirements.txt main.py /workspace/

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install libglu1

CMD ["python", "app.py"]