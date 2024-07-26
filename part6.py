class PeekableIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.next_peek = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_peek is None:
            self.next_value = next(self.iterator)
            return self.next_value
        else:
            self.next_value = self.next_peek
            self.next_peek = None
            return self.next_value

    def peek(self):
        if self.next_peek is None:
            self.next_peek = next(self.iterator)
            return self.next_peek
        else:
            return self.next_peek

    def has_next(self):
        try:
            if self.peek() == self.next_peek:
                return True
        except StopIteration:
            return False
