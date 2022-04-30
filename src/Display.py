import cv2

# globals
outputDir = 'frames'
frameDelay = 42  # the answer to everything


# initialize frame count

def display(g_queue):
    count = 0
    while 1:
        # Read the next frame file
        g_frame = g_queue.dequeue()
        print(f'Displaying frame {count}')

        # Display the frame in a window called "Video"
        cv2.imshow('Video', g_frame)

        # Wait for 42 ms and check if the user wants to quit
        if cv2.waitKey(frameDelay) and 0xFF == ord("q"):
            break

            # get the next frame filename
        count += 1

    # make sure we clean up the windows, otherwise we might end up with a mess
    cv2.destroyAllWindows()
