import binary_search


def test_binary_search():
    test_range = range(-100, 100)
    iterable = range(-50, 50)
    for i in test_range:
        result = binary_search.search(
                iterable, i, binary_search.is_greater, binary_search.is_equal)
        expected = i in iterable
        print i
        assert result == expected
