class Solution:

    def encode(self, strs: List[str]) -> str:
        div = "#"
        result = ""
        
        for s in strs:
            result += str(len(s)) + div + s
        
        return result

    def decode(self, s: str) -> List[str]:
        div = "#"
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != div:
                j += 1
            s_len = int(s[i:j])
            start = j + 1
            end = j + 1 + s_len
            result.append(s[start:end])
            i = end
        
        return result