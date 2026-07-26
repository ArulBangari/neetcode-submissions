class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: set() for i in range(n)}
        visited = set()
        for x, y in edges:
            adjList[x].add(y)
            adjList[y].add(x)

        def dfs(node):
            visited.add(node)
            for child in adjList[node]:
                if child not in visited:
                    dfs(child)

        connected = 0
        for node in adjList:
            if node not in visited:
                connected += 1
                dfs(node)
        return connected