class MinHeap:
    """Binary min-heap stored in a list."""

    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def push(self, value):
        self._items.append(value)
        self._sift_up(len(self._items) - 1)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty heap")

        smallest = self._items[0]
        last = self._items.pop()
        if self._items:
            self._items[0] = last
            self._sift_down(0)
        return smallest

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty heap")
        return self._items[0]

    def _sift_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self._items[index] >= self._items[parent]:
                break
            self._items[index], self._items[parent] = self._items[parent], self._items[index]
            index = parent

    def _sift_down(self, index):
        size = len(self._items)
        while True:
            left = 2 * index + 1
            right = left + 1
            smallest = index

            if left < size and self._items[left] < self._items[smallest]:
                smallest = left
            if right < size and self._items[right] < self._items[smallest]:
                smallest = right
            if smallest == index:
                break

            self._items[index], self._items[smallest] = self._items[smallest], self._items[index]
            index = smallest

    def to_list(self):
        """Return a copy of the underlying array (level-order heap layout)."""
        return list(self._items)
