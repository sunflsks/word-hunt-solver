class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word_end = True
        
    def node_for_prefix(self, prefix):
        node = self

        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
