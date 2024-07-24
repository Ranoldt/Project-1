class PeekableIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.iterator_double = iter(iterable)
        self.next_peek = None
        self.next_value = None
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_peek is None:
            self.next_value = next(self.iterator)
            self.count += 1
            return self.next_value
        else:
            self.next_value = self.next_peek
            self.next_peek = None
            return self.next_value

    def peek(self):
        if self.next_value is None:
            self.next_peek = next(self.iterator)
            self.count += 1
            return self.next_peek
        elif self.next_peek is None:
            self.next_peek = next(self.iterator)
            self.count += 1
            return self.next_peek
        else:
            return self.next_peek

    def has_next(self):
        try:
            for i in range(self.count):
                next(self.iterator_double)
            self.count = 1
            return True
        except StopIteration:
            return False

if __name__ == "__main__":
    x = PeekableIterator(range(3))
    print(next(x))
    print(x.peek())
    print(next(x))
    print(x.has_next())
    print(x.peek())
    print(x.peek())
    print(next(x))
    print(x.has_next())