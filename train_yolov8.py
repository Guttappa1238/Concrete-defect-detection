from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

results = model.train(
        batch=4,
        device="cpu",
        data="/home/iot/Desktop/assignment/dataset/data.yaml",
        epochs=300,
        imgsz=640,
    )