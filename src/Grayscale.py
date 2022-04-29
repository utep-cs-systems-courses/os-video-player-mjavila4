#!/usr/bin/env python3

import cv2

# globals
outputDir = 'frames'


def con_grayscale(e_lock, g_lock, e_queue):
    # initialize frame count
    count = 0

    while not count or (input_frame is not None and count < 72):
        g_lock.acquire()

        while not e_queue:
            pass

        in_file_name = e_queue.pop(0)
        e_lock.release()

        # load the next frame
        input_frame = cv2.imread(in_file_name, cv2.IMREAD_COLOR)

        print(f'Converting frame {count}')

        # convert the image to grayscale
        grayscale_frame = cv2.cvtColor(input_frame, cv2.COLOR_BGR2GRAY)

        # generate output file name
        out_file_name = f'{outputDir}/grayscale_{count:04d}.bmp'

        # write output file
        cv2.imwrite(out_file_name, grayscale_frame)

        count += 1

