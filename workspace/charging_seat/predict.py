
from ultralytics import YOLO
import cv2
# Load a pretrained YOLO11n model
model = YOLO("/home/jiangziben/CodeProject/ultralytics/workspace/charging_seat/runs/detect/train2/weights/best.onnx")

# Run inference on 'bus.jpg'
results = model.predict("/home/jiangziben/Downloads/0000/",stream=True,classes=[0,1])  # results list

# Visualize the results
for i, r in enumerate(results):
    # Plot results image
    im_bgr = r.plot()  # BGR-order numpy array
    # Display the annotated frame
    cv2.imshow("YOLO11 Detect", im_bgr)
    # 按下 'q' 键退出循环
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
 