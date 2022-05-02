import threading

QUEUE_LIMIT = 10


class Queue:

    def __init__(self):
        self.queue = []
        # Signal to other threads that all resources produced/consumed
        self.signal = False

        self.queue_lock = threading.Lock()
        # Amount of resources
        self.fill = threading.Semaphore(0)
        # Queue Bound
        self.empty = threading.Semaphore(QUEUE_LIMIT)

    def enqueue(self, resource):
        self.empty.acquire()
        self.queue_lock.acquire()
        self.queue.append(resource)
        self.queue_lock.release()
        self.fill.release()

    def dequeue(self):
        self.fill.acquire()
        self.queue_lock.acquire()
        resource = self.queue.pop(0)
        self.queue_lock.release()
        self.empty.release()
        return resource

    def is_empty(self):
        return len(self.queue) == 0

    def signal_off(self):
        self.signal = True

    def is_off(self):
        return self.signal
