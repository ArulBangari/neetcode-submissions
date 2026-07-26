class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        res = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if not preMap[crs]:
                if crs not in res:
                    res.append(crs)
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            res.append(crs)
            return True
        
        for crs in preMap:
            if not dfs(crs):
                return []

        return res