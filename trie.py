# -*- coding: utf-8 -*-

class Node(object):

    def __repr__(self):
        return "Node({0}, {1}, {2})".format(
            self.value, self.children, self.is_complete)

    def __str__(self):
        return self.__repr__()

    def __init__(self, value=None):
        self.value = value
        self.children = []
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
            child_values = [child.value for child in node.children]
            if letter in child_values:
                node_index = child_values.index(letter)
                node = node.children[node_index]
            else:
                new_node = Node(letter)
                node.children.append(new_node)
                node = new_node
        node.is_complete = True

    def find(self, key):
        node = self.node
        for letter in key:
            child_values = [child.value for child in node.children]
            try:
                index = child_values.index(letter)
            except ValueError:
                return False
            node = node.children[index]
        return node.is_complete

    def find_all(self, key):
        node = self.node
        for letter in key:
            child_values = [child.value for child in node.children]
            try:
                index = child_values.index(letter)
            except ValueError:
                # No matches
                return []
            node = node.children[index]
        suffixes = self._get_suffixes(node)
        # This repeats the letter at the end of the key.
        return ["".join([key, suffix]) for suffix in suffixes]

    def words(self):
        return self._get_suffixes(self.node)

    def _get_suffixes(self, node):
        """
        return a list of string endings
        """
        all_endings = []
        # Can't str.join None
        value = node.value if node.value is not None else ""
        if len(node.children) == 0:
            return [value]
        for child in node.children:
            endings = self._get_suffixes(child)
            all_endings.extend(
                ["".join([value, ending]) for ending in endings])
        return all_endings


trie = Trie()
trie.insert("hello")
trie.insert("hey")
trie.insert("trie")
print trie
print trie.find("hey")
print trie.find_all("t")
