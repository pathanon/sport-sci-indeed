import cv2
import os
import torch
import numpy as np

from PIL import Image
from tqdm import tqdm

path_video_test = "E:\\test-segment\\test-video-muay-01.mp4"
path_img_test = os.path.join("input_tester",path_video_test.split("\\")[-1][:-4])
os.makedirs(path_img_test,exist_ok=True)
# Load Video File
cap = cv2.VideoCapture(path_video_test)
len_cap = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# Set the number of images selected to test
n = 30  # no. images selected
frame_step = int(len_cap/n)
selected_frame = [c*frame_step for c in range(1,n+1)]
for i in tqdm(range(len_cap)):
    ret, frame = cap.read()
    if i in selected_frame:
        cv2.imwrite(os.path.join(path_img_test,f"{i:06d}.png"), frame)
print("total number of frames : ",len_cap)
print("total number of images selected : ",n)