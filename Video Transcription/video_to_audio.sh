#!/bin/bash

# Define the path to the directory containing the video files
video_dir="/content/drive/MyDrive/BU_fall23/sparkml/project/videos/"

# Define the path to the Python script
python_script="/path/to/diarize_parallel.py"

# Define the whisper model to use
whisper_model="large-v2"

# Loop through video files in the directory
for video_file in "$video_dir"*.mp4; do
    if [ -f "$video_file" ]; then
        echo "Processing $video_file..."
        python "$python_script" -a "$video_file" --whisper-model "$whisper_model"
        echo "Finished processing $video_file"
    fi
done
