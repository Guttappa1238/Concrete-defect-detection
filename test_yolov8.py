from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("/home/iot/Desktop/assignment/runs/segment/train2/weights/best.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
results = model.predict(source="test2.mov", show=True,save=True)