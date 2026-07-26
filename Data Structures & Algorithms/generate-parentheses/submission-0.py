class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return_array = set()
        self.generate(n, 0, 0, "", return_array)
        return list(return_array)
    
    def generate(self, n, o, c, string, return_array):

        if o > n:
            return
        
        if o < c:
            return
        
        if o == c and o == n:
            return_array.add(string)
            return
        
        self.generate(n, o + 1, c, string + "(", return_array)
        self.generate(n, o, c + 1, string + ")", return_array)