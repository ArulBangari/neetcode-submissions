class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        visited = set()

        def dfs(n, prev):
            if n in visited:
                return False
            visited.add(n)
            for child in adjList[n]:
                if prev == child:
                    continue

                if not dfs(child, n):
                    return False
            visited.remove(n)
            return True


        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
            if not dfs(n1, -1):
                return [n1, n2]