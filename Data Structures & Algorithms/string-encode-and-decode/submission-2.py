class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = str(len(strs)) + "#"
        for word in strs:
            ret = ret + str(len(word)) + "#" + word
        return ret

    def decode(self, s: str) -> List[str]:
        char = s[0]
        total_num = ""
        index = 1

        while char != "#":
            total_num += char
            char = s[index]
            index += 1
        ret = ["" for x in range(int(total_num))]

        count = 0
        word_count = 0
        while index < len(s):
            total_num = ""
            char = s[index]
            index += 1
            while char != '#':
                total_num += char
                char = s[index]
                index += 1
            count = int(total_num)
            while count > 0:
                ret[word_count] += s[index]
                index += 1
                count -= 1
            word_count += 1
        return ret