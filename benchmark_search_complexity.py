# -*- coding: utf-8 -*-

import string
import timeit

import bokeh.plotting

import trie_dict


def calculate_trie_complexity(test_case):
    trie.search(test_case)


if __name__ == "__main__":
    trie = trie_dict.Trie()
    trie.insert(string.ascii_letters)

    results = []
    for i, _ in enumerate(string.ascii_letters):
        test_case = string.ascii_letters[:i + 1]
        result = timeit.timeit(
            "calculate_trie_complexity('{}')".format(test_case),
            setup="from __main__ import calculate_trie_complexity")
        print "{}\t{}".format(i + 1, result)
        results.append((i+1, result))

    bokeh.plotting.output_file = "output.html"
    p = bokeh.plotting.figure(
        title="Time complexity of Trie.seach vs search string length, n",
        x_axis_label="n",
        y_axis_label="time")
    p.line(zip(*results)[0], zip(*results)[1], line_width=2)
    bokeh.plotting.show(p)
