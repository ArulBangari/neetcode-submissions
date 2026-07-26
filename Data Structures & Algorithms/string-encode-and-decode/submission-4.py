class Solution:

    def encode(self, strs: List[str]) -> str:
        return_str = "";
        for string in strs:
            return_str += str(len(string)) + "/" + string
        print(return_str)
        return return_str

    def decode(self, s: str) -> List[str]:
        str_length = 0
        index = 0
        strs = []
        while index != len(s):
            start_index = index
            while s[index] != "/":
                index += 1
            end_index = index
            index += 1
            begin_string_index = index
            index += int(s[start_index:end_index])
            end_string_index = index
            strs.append(s[begin_string_index:end_string_index])
        return strs
