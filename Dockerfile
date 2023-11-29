FROM python:3.10.9



WORKDIR /workspace

RUN cd /workspace

COPY . .


# ADD requirements.txt main.py /workspace/

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install libglu1

CMD ["python", "app.py"]
