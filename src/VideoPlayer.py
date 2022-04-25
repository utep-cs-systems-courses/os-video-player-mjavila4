import threading

import Extract


def play():
    extracted_queue = []

    extract_thread = threading.Thread(target=Extract.extract_frames(), args=(extracted_queue, ))


if __name__ == '__main__':
    play()
