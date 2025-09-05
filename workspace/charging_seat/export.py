from ultralytics import YOLO

model = YOLO("/home/jiangziben/CodeProject/ultralytics/workspace/charging_seat/runs/detect/train2/weights/best.pt")  # Load a model
model.export(format="onnx")