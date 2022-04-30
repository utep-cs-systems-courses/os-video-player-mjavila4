#!/usr/bin/env python3

import cv2

clipFileName = '../clip.mp4'

# open the video clip
vid_cap = cv2.VideoCapture(clipFileName)


def extract_frames(e_queue):
    count = 0
    success, image = vid_cap.read()

    while success:
        print(f'Reading frame {count}')
        e_queue.enqueue(image)
        success, image = vid_cap.read()
        count += 1
    e_queue.signal_off()
