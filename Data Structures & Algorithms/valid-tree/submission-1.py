class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        self.count = 0
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        visited = set()
        def dfs(node, prev):
            self.count += 1
            if not adjList[node]:
                return True
            visited.add(node)
            for child in adjList[node]:
                if child == prev:
                    continue
                if child in visited:
                    return False
                if not dfs(child, node):
                    return False
            visited.remove(node)
            return True
    
        if not dfs(0, -1):
            return False
        return self.count == n