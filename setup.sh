#!/bin/bash

echo "Downloading yolov5 repo..."
git clone https://github.com/ultralytics/yolov5.git

echo "Installing python dependencies..."
pip install -r requirements.txt

echo "Downloading dataset..."
bash utils/load_data.sh

echo "Preparing dataset..."
python utils/prepare_data.py

echo "Starting docker container..."
docker run --ipc=host -it --gpus all -v "$(pwd)"/data:/usr/src/data -v  "$(pwd)":/usr/src/project ultralytics/yolov5:latest
