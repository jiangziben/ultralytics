import cv2
import os
from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO("yolo11s.pt")

#folder path
folder_path = "/home/jiangziben/data/MOT17/test/MOT17-01-FRCNN/img1"
image_files = sorted([f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))])
# Loop through the video frames
for image_file in image_files:
    # Read a frame from the video
    image_path = os.path.join(folder_path, image_file)
    frame = cv2.imread(image_path)

    # Run YOLO11 tracking on the frame, persisting tracks between frames
    results = model.track(frame, persist=True,classes=[0])

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow("YOLO11 Tracking", annotated_frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(0) & 0xFF == ord("q"):
        break


# Release the video capture object and close the display window
cv2.destroyAllWindows()