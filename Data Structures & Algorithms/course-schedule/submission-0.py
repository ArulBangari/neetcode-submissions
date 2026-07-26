class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if not preMap[crs]:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                preMap[crs].remove(pre)
            visited.remove(crs)
            return True
        
        for crs in preMap:
            if not dfs(crs):
                return False

        return True