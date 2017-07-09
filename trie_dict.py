# -*- coding: utf-8 -*-

class Node(object):

    def __repr__(self):
        return "Node({0}, {1}, {2})".format(
            self.value, self.children, self.is_complete)

    def __str__(self):
        return self.__repr__()

    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.is_complete = False


class Trie(object):

    def __init__(self):
        self.node = Node()

    def __repr__(self):
        return self.node.__repr__()

    def __str__(self):
        return self.__repr__()

    def insert(self, key):
        node = self.node
        for letter in key:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = Node(letter)
                node.children[letter] = new_node
                node = new_node
        node.is_complete = True

    def find(self, key):
        node = self.node
        for letter in key:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]
        return node.is_complete

    def search(self, key):
        node = self.node
        for letter in key:
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]
        return True


if __name__ == "__main__":
    trie = Trie()
    with open("words") as word_file:
        i = 0
        for line in word_file:
            if i > 10:
                break
            trie.insert(line)
            i += 1
    print trie
    print trie.find("zebr")

# trie = Trie()
# trie.insert("hello")
# trie.insert("hey")
# trie.insert("trie")
# print trie
# print trie.find("hey")
