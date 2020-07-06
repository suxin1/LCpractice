
from threading import Lock
class CircularQueue(object):
    def __init__(self, k):
        self.queue = [0] * k
        self.head = 0
        self.count = 0
        self.capacity = k
        self.queueLock = Lock()
    
    def enQueue(self, value):
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.head + self.count)%self.capacity] = value
            self.count += 1
        return True

    def deQueue(self):
        with self.queueLock:
            if self.count == 0:
                return False
            self.head = (self.head + 1) % self.capacity
            self.count -= 1
        return True
    
    def Front(self):
        if self.count == 0:
            return -1
        return self.queue[self.head]

    def Rear(self):
        if self.count == 0:
            return -1
        return self.queue[(self.head + self.count - 1)%self.capacity]
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
def test():
    cq = CircularQueue(4)
    cq.enQueue(1)
    cq.enQueue(3)
    cq.enQueue(6)
    cq.enQueue(8)
    cq.enQueue(12)
    cq.deQueue()
    cq.enQueue(12)
    cq.deQueue()
    cq.deQueue()
    cq.deQueue()
    cq.deQueue()

test()