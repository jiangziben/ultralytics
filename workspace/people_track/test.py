import cv2
import os
from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO("yolo11s.pt")

#folder path
# folder_path = "/home/jiangziben/data/MOT17/test/MOT17-01-FRCNN/img1"
# image_files = sorted([f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))])
# Loop through the video frames
# for image_file in image_files:
#     # Read a frame from the video
#     image_path = os.path.join(folder_path, image_file)
#     frame = cv2.imread(image_path)

#     # Run YOLO11 tracking on the frame, persisting tracks between frames
#     results = model.track(frame, persist=True,classes=[0], tracker="bytetrack.yaml")

#     # Visualize the results on the frame
#     annotated_frame = results[0].plot()

#     # Display the annotated frame
#     cv2.imshow("YOLO11 Tracking", annotated_frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(0) & 0xFF == ord("q"):
#         break


# Release the video capture object and close the display window
# cv2.destroyAllWindows()

import cv2

# 读取视频文件
cap = cv2.VideoCapture('/home/jiangziben/data/people_tracking/gait/20241030_165339.mp4')

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# 循环读取视频帧
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 显示当前帧
    # Run YOLO11 tracking on the frame, persisting tracks between frames
    results = model.track(frame, persist=True,classes=[0], tracker="botsort.yaml")

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLO11 Tracking", annotated_frame)
    # 按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()