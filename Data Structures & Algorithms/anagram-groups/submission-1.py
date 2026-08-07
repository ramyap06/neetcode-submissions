class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_dicts = {}
        anagrams = []

        def make_word_count(word):
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            return tuple(count)
        
        def make_new_anagram_list(word, word_count):
            anagrams.append([word])
            char_dicts[word_count] = len(anagrams) - 1 

        for word in strs:
            if not char_dicts:
                make_new_anagram_list(word, make_word_count(word))
                continue
            
            wc = make_word_count(word)

            if wc in char_dicts:
                anagrams[char_dicts[wc]].append(word)
            else:
                make_new_anagram_list(word, make_word_count(word))
    
        return anagrams