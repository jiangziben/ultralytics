
from ultralytics import YOLO
import cv2
# Load a pretrained YOLO11n model
model = YOLO("/home/jiangziben/CodeProject/ultralytics/workspace/people_track/yolo11m.pt")

# Run inference on 'bus.jpg'
results = model.predict("/home/jiangziben/data/people/Zhangzhaokang/Color",stream=True,classes=[0])  # results list

# Visualize the results
for i, r in enumerate(results):
    # Plot results image
    im_bgr = r.plot()  # BGR-order numpy array
    # Display the annotated frame
    cv2.imshow("YOLO11 Tracking", im_bgr)
    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
