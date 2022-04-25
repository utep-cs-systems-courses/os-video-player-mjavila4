#!/usr/bin/env python3

import cv2
import os

# globals
import Extract

outputDir = 'frames'
clipFileName = '../clip.mp4'

# open the video clip
vid_cap = cv2.VideoCapture(clipFileName)


def extract_frames(q):
    # initialize frame count
    count = 0
    # create the output directory if it doesn't exist
    if not os.path.exists(outputDir):
        print(f"Output directory {outputDir} didn't exist, creating")
        os.makedirs(outputDir)

    # read one frame
    success, image = vid_cap.read()

    print(f'Reading frame {count} {success}')
    while success and count < 72:
        # write the current frame out as a jpeg image
        cv2.imwrite(f"{outputDir}/frame_{count:04d}.jpg", image)


        success, image = vid_cap.read()
        print(f'Reading frame {count}')
        count += 1
