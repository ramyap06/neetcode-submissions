class TrieNode:
    def __init__(self):
        self.word = ''
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        result = set()
        
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(row, col, root):
            if root.word != '' and root.word not in result:
                result.add(root.word)
            if (row < 0 or col < 0 or
                row >= ROWS or col >= COLS or
                board[row][col] not in root.children):
                return
            
            temp = board[row][col]
            board[row][col] = '*'

            dfs(row + 1, col, root.children[temp])
            dfs(row - 1, col, root.children[temp])
            dfs(row, col + 1, root.children[temp])
            dfs(row, col - 1, root.children[temp])
            
            board[row][col] = temp
        
        for r in range(ROWS):
            for c in range(COLS):
                if len(words) == len(result):
                    return list(result)
                dfs(r, c, trie.root)
        
        return list(result)