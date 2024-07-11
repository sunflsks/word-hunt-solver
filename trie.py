class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        # only reached when nodes have been traversed all the way to the end
        node.word_end = True

    def node_for_prefix(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
