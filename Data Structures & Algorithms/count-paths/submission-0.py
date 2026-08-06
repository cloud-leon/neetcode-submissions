class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        def dfs(r,c):
            nonlocal count
            if r < 0 or c< 0 or r> m or c >n:
                return
            if r==m-1 and c == n-1:
                count +=1
            dfs(r+1,c)
            dfs(r,c+1)
        
        dfs(0,0)
        return count