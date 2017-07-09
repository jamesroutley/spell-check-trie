# -*- coding: utf-8 -*-

import pytest

from trie import Trie

def pre_populated_trie():
    trie = Trie()
    trie.insert("hello")
    trie.insert("hey")
    trie.insert("trie")
    return trie

@pytest.mark.parametrize("key,result", [
    ("hello", True),
    ("foo", False)
])
def test_find(key, result):
    trie = pre_populated_trie()
    assert trie.find(key) == result
