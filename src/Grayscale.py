#!/usr/bin/env python3

import cv2

# globals
outputDir = 'frames'


def con_grayscale(e_queue, g_queue):
    # initialize frame count
    count = 0

    while 1:
        extracted_frame = e_queue.dequeue()
        print(f'Converting frame {count}')

        grayscale_frame = cv2.cvtColor(extracted_frame, cv2.COLOR_BGR2GRAY)

        g_queue.enqueue(grayscale_frame)
        # print(f'Frame {count} Successfully Enqueued')

        count += 1
