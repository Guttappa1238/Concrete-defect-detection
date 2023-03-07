# Concrete-defect-detection
Concrete defect analysis
1. Analyse the type of defect (Crack, Spalling, rebar)
2. Segment individual defects along with confidence rate.


# Why  I Used YOLOv8?
Here are a few main reasons why i consider using YOLOv8 for this work:
    1. YOLOv8 has a high rate of accuracy measured by COCO and Roboflow 100.
    2. YOLOv8 comes with a lot of developer-convenience features, from an easy-to-use CLI to a well-structured Python package.
    3. There is a large community around YOLO and a growing community around the YOLOv8 model, meaning there are many people in computer vision circles who may be able to assist you when you need guidance.

YOLOv8 Architecture:
    • Backbone: New CSP-Darknet53 
    • Neck: SPPF, New CSP-PAN 
    • Head: YOLOv3 Head 

![image](https://user-images.githubusercontent.com/45628395/223023013-dfc0944c-8f43-4e8b-8633-341be131fba3.png)



# Anchor Free Detection
YOLOv8 is an anchor-free model. This means it predicts directly the center of an object instead of the offset from a known anchor box.

![image](https://user-images.githubusercontent.com/45628395/223023057-fda8b42b-b13f-4eef-bdc5-6b2dd3f060f5.png)


# Dataset information:
	The dataset consist of 396 images in total and split into train and valid sets, which also have the labels. I used Roboflow to label the images.

# Training And Results:

	In this work i have used nano pretrained model. And it gave good results in real time inference.
	
	for trainig run python3 train_yolov8.py
	
	for testing run python3 test_yolov8.py

![image](https://user-images.githubusercontent.com/45628395/223023120-b7fb104f-8b3b-402c-b978-9ae662430f20.png)

![image](https://user-images.githubusercontent.com/45628395/223023260-bd1a5ff1-541c-422a-9c3d-73aaeea7643b.png)

# Confusion matrix:
![image](https://user-images.githubusercontent.com/45628395/223023280-90c07b32-272a-4313-875c-c3ea82ae0082.png)



# Results:
![image](https://user-images.githubusercontent.com/45628395/223023299-6105a266-a430-4838-bff2-4d5fbcc4651b.png)

