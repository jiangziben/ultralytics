from ultralytics import YOLO

# Configure the tracking parameters and run the tracker
model = YOLO("yolo11m-pose.pt")
results = model.track(source="/home/jiangziben/data/people_tracking/3d/follow/Color", conf=0.3, iou=0.5, save=True)