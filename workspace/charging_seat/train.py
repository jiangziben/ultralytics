from ultralytics import YOLO

# Load a model
model = YOLO("/home/jiangziben/CodeProject/ultralytics/workspace/charging_seat/yolo11s.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="/home/jiangziben/CodeProject/ultralytics/ultralytics/cfg/datasets/charging_seat.yaml", 
                      epochs=100, 
                      imgsz=640,
                      bgr=0.5,
                      cutmix=0.5,
                      )