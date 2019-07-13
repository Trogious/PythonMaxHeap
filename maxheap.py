
class MaxHeap:
    def __init__(self):
        self.h = []
        self.positions = {}

    def push(self, item):
        self.h.append(item)
        i = len(self.h)-1
        while self.h[i] > self.h[MaxHeap._parent(i)]:
            self._swap(i, MaxHeap._parent(i))
            i = MaxHeap._parent(i)
        self.positions[item] = i

    def pop(self, item):
        i = self.index(item)
        if i < 0:
            return
        while not self._is_leaf(i):
            
        self.h.remove(len(self.h)-1)

    def peek(self):
        return self.h[0]

    def index(self, item):
        if item in self.positions:
            return self.positions[item]
        else:
            return -1

    def _heapify(self, i):
        if not self._is_leaf(i):
            if self.h[i] < self.h[MaxHeap._left(i)] or self.h[i] < self.h[MaxHeap._right(i)]:
                if self.h[MaxHeap._left(i)] > self.h[MaxHeap._right(i)]:
                    self._swap(i, MaxHeap._left(i))
                    self._heapify(MaxHeap._left(i))
                else:
                    self._swap(i, MaxHeap._right(i))
                    self._heapify(MaxHeap._right(i))

    def _swap(self, i, j):
        self.h[i], self.h[j] = self.h[j], self.h[i]

    def _is_leaf(self, i):
        size = len(self.h)
        return i >= (size / 2) and i <= size

    @staticmethod
    def _left(i):
        return i*2+1

    @staticmethod
    def _right(i):
        return i*2+2

    @staticmethod
    def _parent(i):
        return int((i-1)/2)


mh = MaxHeap()
for x in [30, 10, 5, 4, 3, 32, 21]:
    mh.push(x)
print(mh.peek())
print(mh.index(7))
print(mh.h)
