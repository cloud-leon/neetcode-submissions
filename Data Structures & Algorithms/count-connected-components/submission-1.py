class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = defaultdict(list)
        seen = set()
        count = 0
        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        
        
        def dfs(i):
            seen.add(i)
            for neighbor in adjlist[i]:
                if neighbor not in seen:
                    dfs(neighbor)

        for i in range(n):
            if i not in seen:
                count+=1
                dfs(i)
        return count