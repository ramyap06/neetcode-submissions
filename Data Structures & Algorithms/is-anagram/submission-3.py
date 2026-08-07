class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letter_dict = {}

        for c in s:
            if c not in letter_dict:
                letter_dict[c] = 0
            letter_dict[c] += 1
        
        for i in t:
            if i not in letter_dict or letter_dict[i] == 0:
                return False
            
            letter_dict[i] -= 1
        return True
            