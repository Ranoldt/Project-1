class PeekableIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        return self.iterator[self.count]

    def peek(self):
        pass

    def has_next(self):
        try:
            self.peek()
            return True
        except StopIteration:
            return False


