from collections import deque
from typing import Any


class LRU:
    def __init__(self, size: int):
        self.elements = set()
        self.size = size
        self.queue = deque(maxlen=size)

    def push(self, val: Any):
        if val not in self.elements:
            if len(self.elements) >= self.size:
                element = self.queue.popleft()
                self.elements.remove(element)

            self.elements.add(val)
            self.queue.append(val)
        else:
            self.queue.remove(val)
            self.queue.append(val)

    def clear(self):
        self.elements.clear()
        self.queue.clear()

    def __iter__(self):
        yield from self.queue

    def __reversed__(self):
        yield from reversed(self.queue)

    def __repr__(self):
        return f"{list(self.queue)}"


if __name__ == '__main__':
    lru = LRU(9)

    for i in range(15):
        lru.push(i)

    print(lru)
    lru.push(8)
    print(lru)
    lru.push(20)
    print(lru)
