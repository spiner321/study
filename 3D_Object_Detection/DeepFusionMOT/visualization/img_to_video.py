# -*-coding:utf-8-*
# author: wangxy
import cv2
import os

'''
	This code is converting images to video.
'''
# Write your folder path here，example：/home/youname/data/img/
# Note that the last folder should have a /
os.makedirs('/content/drive/MyDrive/workspace/study/3D_Object_detection/DeepFusionMOT/results/train/video', exist_ok = True)
img_root = '../results/train/image/0000/'
video_save_path = '../results/train/video/' + img_root[-5:-1] + '.avi'
fps = 12
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
videoWriter = cv2.VideoWriter(video_save_path,fourcc,fps, (1242,375))

# for i in range(297):  # Here 297 is the number of frames in the dataset. You need to make the appropriate changes
# 	number = '%06d'%i
# 	frame = cv2.imread(img_root+number+'.png')
# 	videoWriter.write(frame)

frames = os.listdir(img_root)
for frame in frames:
    frame = cv2.imread(img_root + frame)
    videoWriter.write(frame)
videoWriter.release()
