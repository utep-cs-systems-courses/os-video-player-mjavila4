import threading
import Extract
import Grayscale


def play():
    e_locks = threading.Semaphore(10)
    g_locks = threading.Semaphore(10)
    extract_queue = []

    extract_thread = threading.Thread(target=Extract.extract_frames, args=(e_locks, extract_queue))
    con_grayscale_thread = threading.Thread(target=Grayscale.con_grayscale, args=(e_locks, g_locks, extract_queue))

    extract_thread.start()
    con_grayscale_thread.start()


if __name__ == '__main__':
    play()
