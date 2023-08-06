
## Requirements

```bash
  Python >= 3.8
  Docker
  Nvidia Docker & Nvidia Container Toolkit (if working on a system with GPU)
```

You can make use of conda env
```bash
  conda create --name fruit_detection python=3.8
  conda activate fruit_detection
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/evgeniishch/fruit_detection.git
```

Go to the project directory

```bash
  cd fruit_detection
```

Run setup

```bash
  bash setup.sh
```

To train the model, inside the container run

```bash
  python train.py --img 320 --rect --epochs 9 --data ../project/data_conf.yaml --weights yolov5s.pt
```

For inference on sample data, inside the container run

```bash
   python detect.py --source ../data/images/test --weights runs/train/exp/weights/best.pt
```
