class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {} # char : TrieNode

class PrefixTree:

    def __init__(self):
        self.root = TrieNode('^')

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.children['*'] = TrieNode('*')

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        if '*' not in curr.children:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True