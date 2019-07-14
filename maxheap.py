
class MaxHeap:
    def __init__(self):
        self.h = []
        self._positions = {}
        self._size = 0

    def empty(self):
        return self._size < 1

    def size(self):
        return self._size

    def peek(self):
        return self.h[0]

    def push(self, item):
        try:
            exists = item in self._positions
        except KeyError:
            exists = False
        if not exists:  # do not allow duplicates
            self.h.append(item)
            self._size += 1
            i = self._size-1
            self._add_position(item, i)
            while self.h[i] > self.h[MaxHeap._parent(i)]:
                self._swap(i, MaxHeap._parent(i))
                i = MaxHeap._parent(i)

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
        self._remove_position(item)

    def _remove_position(self, item):
        del self._positions[item]

    def _add_position(self, item, i):
        self._positions[item] = i

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
        assert (self.h[i] != self.h[j]), 'h[i]==h[j]'
        # print('swap: %s <-> %s' % (self._positions[self.h[i]], self._positions[self.h[j]]))
        self._positions[self.h[i]], self._positions[self.h[j]] = j, i
        # print('swapped: %s <-> %s' % (self._positions[self.h[i]], self._positions[self.h[j]]))
        self.h[i], self.h[j] = self.h[j], self.h[i]

    def _is_leaf(self, i):
        return i >= (self._size / 2) and i <= self._size

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
    pos = mh._print_pos()
    mh.remove(x)
    print(mh.h)
    print(pos)


if __name__ == '__main__':
    mh = MaxHeap()
    for x in [30, 10, 5, 4, 3, 32, 21]:
        mh.push(x)
    print('REMOVING START 1')
    test_remove(mh, 3)
    test_remove(mh, 32)
    test_remove(mh, 5)
    test_remove(mh, 4)
    test_remove(mh, 30)
    for x in [12, 43, 15]:
        mh.push(x)
    print('REMOVING START 2')
    test_remove(mh, 10)
    test_remove(mh, 21)
    test_remove(mh, 43)
    test_remove(mh, 15)
    test_remove(mh, 12)
    print(mh._print_pos())
    for x in [20, 20, 21, 20]:
        mh.push(x)
    print(mh._print_pos())
    print('REMOVING START 3')
    test_remove(mh, 20)
    try:
        test_remove(mh, 20)
        test_remove(mh, 20)
    except KeyError:
        pass
    test_remove(mh, 21)
    for x in [30, 5, 10, 5]:
        mh.push(x)
    print(mh.h)
    test_remove(mh, 30)
