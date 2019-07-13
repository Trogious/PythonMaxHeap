
class MaxHeap:
    def __init__(self):
        self.h = []
        self._positions = {}
        self._size = 0

    def empty(self):
        return len(self.h) < 1

    def push(self, item):
        self.h.append(item)
        self._size += 1
        i = self._size-1
        while self.h[i] > self.h[MaxHeap._parent(i)]:
            self._swap(i, MaxHeap._parent(i))
            i = MaxHeap._parent(i)
        self._positions[item] = i

    def pop(self):
        top = self.h[0]
        self._remove(0)
        return top

    def remove(self, item):
        self._remove(self._index(item))

    def _remove(self, i):
        item = self.h[i]
        if i < self._size-1:
            self._swap(i, self._size-1)
            self.h.pop()
            self._size -= 1
            self._heapify(i)
        else:
            self.h.pop()
            self._size -= 1
        del self._positions[item]

    def peek(self):
        return self.h[0]

    def _index(self, item):
        return self._positions[item]

    def _heapify(self, i):
        if not self._is_leaf(i):
            left = MaxHeap._left(i)
            right = MaxHeap._right(i)
            if left < self._size and self.h[i] < self.h[left]:
                if right < self._size and self.h[i] < self.h[right]:
                    if self.h[left] > self.h[right]:
                        self._swap(i, left)
                        self._heapify(left)
                    else:
                        self._swap(i, right)
                        self._heapify(right)
                else:
                    self._swap(i, left)
                    self._heapify(left)

    def _swap(self, i, j):
        self._positions[self.h[i]], self._positions[self.h[j]] = j, i
        self.h[i], self.h[j] = self.h[j], self.h[i]

    def _is_leaf(self, i):
        size = len(self.h)
        return i >= (size / 2) and i <= size

    def _print_pos(self):
        pos = ''
        for k in self._positions.keys():
            pos += 'h[%d]=%d ' % (self._positions[k], k)
        return pos

    @staticmethod
    def _left(i):
        return i*2+1

    @staticmethod
    def _right(i):
        return i*2+2

    @staticmethod
    def _parent(i):
        return int((i-1)/2)


def test_remove(mh, x):
    import sys
    sys.stdout.write('removing: %d, %s -> ' % (x, str(mh.h)))
    # pos = mh._print_pos()
    mh.remove(x)
    print(mh.h)
    # print(pos)


mh = MaxHeap()
for x in [30, 10, 5, 4, 3, 32, 21]:
    mh.push(x)
test_remove(mh, 3)
test_remove(mh, 32)
test_remove(mh, 5)
test_remove(mh, 4)
test_remove(mh, 30)
for x in [12, 43, 15]:
    mh.push(x)
test_remove(mh, 10)
test_remove(mh, 21)
test_remove(mh, 43)
test_remove(mh, 15)
test_remove(mh, 12)
