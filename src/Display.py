import cv2

# globals
frameDelay = 42  # the answer to everything


def display(g_queue):
    count = 0
    while not g_queue.is_off() or not g_queue.is_empty():
        print(f'Displaying frame {count}')
        # Read the next frame file
        g_frame = g_queue.dequeue()

        # Display the frame in a window called "Video"
        cv2.imshow('Video', g_frame)

        # Wait for 42 ms and check if the user wants to quit
        if cv2.waitKey(frameDelay) and 0xFF == ord("q"):
            break

        count += 1

    # make sure we clean up the windows, otherwise we might end up with a mess
    cv2.destroyAllWindows()
