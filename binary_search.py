# -*- coding: utf-8 -*-


def search(iterable, key, is_greater, is_equal):
    def _binary_search(lower, upper):
        # Assume Python 2 integer division
        midpoint = (upper + lower) / 2
        if is_equal(key, iterable[midpoint]):
            return True
        if upper - lower <= 1:
            return False
        if is_greater(key, iterable[midpoint]):
            return _binary_search(midpoint + 1, upper)
        else:
            return _binary_search(lower, midpoint)

    if is_greater(key, iterable[-1]):
        return False
    if is_greater(iterable[0], key):
        return False
    return _binary_search(0, len(iterable))


def is_greater(a, b):
    return a > b


def is_equal(a, b):
    return a == b


if __name__ == "__main__":
    print search(range(-50, 50), -49, is_greater, is_equal)
