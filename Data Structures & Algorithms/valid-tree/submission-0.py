class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        visited = set()
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
        
        self.count = 0
        def dfs(node, parent):
            self.count += 1
            if not adjList[node]:
                return True
            visited.add(node)
            for child in adjList[node]:
                if child == parent:
                    continue
                print(parent, node, child)
                if child in visited:
                    print(child)
                    return False
                
                dfs(child, node)
            visited.remove(node)
            return True

        if not dfs(0, -1):
            return False
        return self.count == n