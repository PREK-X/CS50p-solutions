class Jar:
    def __init__(self, capacity = 12, size = 0):
        if size > capacity or size < 0 or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = size

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if n < 0 or self.size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if n < 0 or n > self.size:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
