class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for word in strs:
            ret += str(len(word)) + "*" + word
        return ret

    def decode(self, s: str) -> List[str]:
        i = 0
        ret = []
        while i < len(s):
            numBeg = i
            while s[i] != "*":
                i += 1
            num = int(s[numBeg: i])
            i += 1
            ret.append(s[i: i + num])
            i += num
        return ret