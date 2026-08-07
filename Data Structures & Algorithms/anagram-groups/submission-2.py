class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            count = [0] * 26
            
            for c in word:
                index = ord(c) - ord("a")
                count[index] += 1
            key = tuple(count)

            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
            
        return list(anagrams.values())