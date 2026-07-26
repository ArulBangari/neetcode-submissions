class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        visit = set()
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for child in adjList[node]:
                dfs(child)
        
        count = 0
        for node in adjList:
            if node not in visit:
                count += 1
                dfs(node)
        return count