class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indices = [0]
        ret = [0 for x in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            print(indices)
            while len(indices) != 0 and temperatures[indices[-1]] < temperatures[i]:
                x = indices.pop()
                ret[x] = i - x
            indices.append(i)

        return ret