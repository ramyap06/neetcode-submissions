class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('^')

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.children['*'] = TrieNode('*')

    def search(self, word: str) -> bool:
        def dfs(node, c):
            if c == len(word):
                return '*' in node.children
            
            if word[c] != '.':
                if word[c] not in node.children:
                    return False
                return dfs(node.children[word[c]], c + 1)
            else:
                for child in node.children.values():
                    if child.char != '*' and dfs(child, c + 1):
                        return True
            return False
        
        return dfs(self.root, 0)