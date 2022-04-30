import threading

QUEUE_LIMIT = 10


class Queue:
    queue = []

    queue_lock = threading.Lock()

    fill = threading.Semaphore(0)
    empty = threading.Semaphore(QUEUE_LIMIT)

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
