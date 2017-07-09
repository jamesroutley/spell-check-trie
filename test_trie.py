# -*- coding: utf-8 -*-

import pytest

from trie_dict import Trie

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

@pytest.mark.parametrize("key,result", [
    ("hello", True),
    ("hel", True),
    ("foo", False)
])
def test_search(key, result):
    trie = pre_populated_trie()
    assert trie.find(key) == result


