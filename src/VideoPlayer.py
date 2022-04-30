import threading
import Extract
import Grayscale
import Display
import Queue


def play():

    e_queue = Queue.Queue()
    g_queue = Queue.Queue()

    extract_thread = threading.Thread(target=Extract.extract_frames, args=(e_queue, ))
    con_grayscale_thread = threading.Thread(target=Grayscale.con_grayscale, args=(e_queue, g_queue))
    display_thread = threading.Thread(target=Display.display, args=(g_queue, ))

    extract_thread.start()
    con_grayscale_thread.start()
    display_thread.start()


if __name__ == '__main__':
    play()

