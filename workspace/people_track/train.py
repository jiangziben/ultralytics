from ultralytics import YOLO

# Load a model
model = YOLO("yolo11m.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="/home/jiangziben/CodeProject/ultralytics/ultralytics/cfg/datasets/people_tracking.yaml", 
                      epochs=100, 
                      imgsz=640,
                      )