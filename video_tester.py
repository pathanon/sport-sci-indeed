import cv2
import numpy as np
import os
import torch
from ultralytics import YOLO


torch.cuda.set_device(0)
model_det = YOLO("model/best-weight2/best-v6-200.pt")
# check video

################################

cap = cv2.VideoCapture("E:\\test-segment\\test-video-muay-01.mp4")
# cap = cv2.VideoCapture("input/test_action_extraction.avi")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
cap.set(cv2.CAP_PROP_FPS, 60)
fps = int(cap.get(5))
# out = cv2.VideoWriter("E:\\result_muay03-v1-200.mp4",cv2.VideoWriter_fourcc(*'mp4v'), fps,(frame_width,frame_height))
out = cv2.VideoWriter("E:\\test-segment\\results\\s-v6-200.mp4",cv2.VideoWriter_fourcc(*'mp4v'), fps,(frame_width,frame_height))

################################
while cap.isOpened():
    check, frame = cap.read()
    
    results_det = model_det(frame,classes=[0,1])
    draw_frame = results_det[0].plot(boxes=False)
    # draw_frame = postprocess_prediction(results_det[0], cls_cmap)

    cv2.imshow("output", draw_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    out.write(draw_frame)

cap.release()
cv2.destroyAllWindows()
