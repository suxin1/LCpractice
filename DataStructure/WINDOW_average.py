from collections import deque


class MovingAverage(object):
    count = 0
    sum = 0

    def __init__(self, size: int):
        self.size = size
        self.queue = deque(maxlen=size)

    def next(self, number: int):
        if self.count < self.size:
            self.count += 1
            self.sum += number
        else:
            self.sum += number - self.queue.popleft()

        self.queue.append(number)
        return self.sum / self.count


ma = MovingAverage(3)

print(ma.next(1))
print(ma.next(10))
print(ma.next(3))
print(ma.next(5))