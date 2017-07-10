import cProfile

import trie_dict


def initialise_trie():
    trie = trie_dict.Trie()
    for word in words:
        trie.insert(word)

if __name__ == "__main__":
    with open("words") as word_file:
        words = word_file.readlines()
    words = [word.strip() for word in words]

    cProfile.run("initialise_trie()")
