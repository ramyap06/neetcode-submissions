class Solution:

    def encode(self, strs: List[str]) -> str:
        full_string = ""
        for string in strs:
            length = len(string)
            full_string += str(length) + "?" + string
        return full_string

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        word_list = []

        while i < n:
            j = i
            word = ""

            while s[j] != "?":
                j += 1
            length = int(s[i:j])
            i = j + 1

            word = s[i:i + length]
            word_list.append(word)
            i += length

        return word_list
