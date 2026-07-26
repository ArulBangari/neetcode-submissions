class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adjList = defaultdict(list)
        out = defaultdict(int)
        for src, dest in tickets:
            adjList[src].append(dest)
            out[src] += 1
        
        res = []
        def dfs(src):
            while out[src]:
                out[src] -= 1
                dest = adjList[src][out[src]]
                dfs(dest)
            res.append(src)
        dfs("JFK")
        res.reverse()
        return res
