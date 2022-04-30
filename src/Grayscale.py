#!/usr/bin/env python3

import cv2


def con_grayscale(e_queue, g_queue):
    count = 0

    while not e_queue.is_off() or not e_queue.is_empty():
        print(f'Converting frame {count}')
        extracted_frame = e_queue.dequeue()
        grayscale_frame = cv2.cvtColor(extracted_frame, cv2.COLOR_BGR2GRAY)
        g_queue.enqueue(grayscale_frame)
        count += 1
    g_queue.signal_off()
