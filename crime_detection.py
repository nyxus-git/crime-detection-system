import torch
import cv2
import numpy as np

# Load the pretrained YOLOv5 model from the local repository
model = torch.hub.load('/home/nyxus/Documents/crime-detection-system/yolov5', 'custom', path='/home/nyxus/Documents/crime-detection-system/best.pt', source='local')

# Access the camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the frame
    results = model(frame)

    # Render the results on the frame
    frame_with_detections = np.squeeze(results.render())

    # Display the frame
    cv2.imshow('Crime Detection System', frame_with_detections)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
