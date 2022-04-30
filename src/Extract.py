#!/usr/bin/env python3

import cv2
import os

# globals
import Extract

outputDir = 'frames'
clipFileName = '../clip.mp4'

# open the video clip
vid_cap = cv2.VideoCapture(clipFileName)


def extract_frames(e_queue):
    # initialize frame count
    count = 0

    while count < 1:
        print(f'Reading frame {count}')
        # write the current frame out as a jpeg image
        success, image = vid_cap.read()
        e_queue.enqueue(image)
        count += 1
