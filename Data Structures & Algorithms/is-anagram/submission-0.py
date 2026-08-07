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
            if i not in letter_dict:
                return False
            letter_dict[i] -= 1
            
            # must be after because if it was before then if its a valid anagram
            # it would never reach that if statement & would never deleted empty keys
            if letter_dict[i] == 0:
                del letter_dict[i]
        
        if letter_dict:
            return False
        return True
            