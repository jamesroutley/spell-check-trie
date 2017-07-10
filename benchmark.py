# -*- coding: utf-8 -*-

import random
import timeit

import pympler.asizeof

import binary_search
import trie_dict


def is_greater(a, b):
    return a > b


def is_equal(a, b):
    return b.startswith(a)


def benchmark_binary_search():
    for case in test_cases:
        binary_search.search(words, case, is_greater, is_equal)


def benchmark_trie():
    for case in test_cases:
        trie.search(case)


if __name__ == "__main__":
    num_tries = 100
    num_samples = 1000

    with open("words") as word_file:
        words = word_file.readlines()

    words = [word.strip() for word in words]
    words.sort()

    test_cases = random.sample(words, num_samples)

    trie = trie_dict.Trie()
    for word in words:
        trie.insert(word)

    print "starting tests"

    result = timeit.timeit(
        "benchmark_binary_search()",
        setup="from __main__ import benchmark_binary_search",
        number=num_tries)
    print "Binary search {} items {} times: {}".format(
        num_samples, num_tries, result)

    result = timeit.timeit(
        "benchmark_trie()",
        setup="from __main__ import benchmark_trie",
        number=num_tries)
    print "Trie search {} items {} times: {}".format(
        num_samples, num_tries, result)

    print "Word list size: {}".format(pympler.asizeof.asizeof(words))
    print "Trie size: {}".format(pympler.asizeof.asizeof(trie))
