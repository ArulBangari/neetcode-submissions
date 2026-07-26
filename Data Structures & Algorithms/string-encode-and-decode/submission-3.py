class Solution:

    def encode(self, strs: List[str]) -> str:
        return_str = str(len(strs)) + "|"
        for string in strs:
            return_str += str(len(string)) + "|" + string
        return return_str

    def decode(self, s: str) -> List[str]:
        ind = 0
        return_arr = ["" for _ in range(int(s[:s.find("|")]))]
        s_copy = s[s.find("|") + 1:]
        for i in range(len(return_arr)):
            len_string = int(s_copy[:s_copy.find("|")])
            s_copy = s_copy[s_copy.find("|") + 1:]
            return_arr[i] += s_copy[:len_string]
            s_copy = s_copy[len_string:]
        return return_arr
