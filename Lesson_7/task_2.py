class frange:
    def __init__(self, start, stop=None, step=1.0):
        if stop is None:
            start, stop = 0.0, start
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        if self.step > 0:
            current = self.start
            while current < self.stop:
                yield current
                current += self.step
        elif self.step < 0:
            current = self.start
            while current > self.stop:
                yield current
                current += self.step


if __name__ == '__main__':
    test_cases = [
        (list(frange(5)), [0, 1, 2, 3, 4]),
        (list(frange(2, 5)), [2, 3, 4]),
        (list(frange(2, 10, 2)), [2, 4, 6, 8]),
        (list(frange(10, 2, -2)), [10, 8, 6, 4]),
        (list(frange(2, 5.5, 1.5)), [2, 3.5, 5]),
        (list(frange(1, 5)), [1, 2, 3, 4]),
        (list(frange(0, 5)), [0, 1, 2, 3, 4]),
        (list(frange(0, 0)), []),
        (list(frange(100, 0)), [])
    ]

    success = True
    for idx, (actual, expected) in enumerate(test_cases):
        if actual != expected:
            success = False
            print(f'Test case {idx + 1} failed: Expected {expected}, '
                  f'but got {actual}')

    if success:
        print('SUCCESS!')


for i in frange(1, 100, 3.5):
    print(i)
