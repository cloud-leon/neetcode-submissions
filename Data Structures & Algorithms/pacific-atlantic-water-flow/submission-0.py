class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()


        def dfs(r,c,curlist,prevheight):
            if (r<0 or r >= ROWS
            or c<0 or c>= COLS or 
            heights[r][c] < prevheight or (r,c) in curlist):
                return
            
            curlist.add((r,c))
            dfs(r+1,c,curlist,heights[r][c])
            dfs(r-1,c,curlist,heights[r][c])
            dfs(r,c+1,curlist,heights[r][c])
            dfs(r,c-1,curlist,heights[r][c])


        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])

        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
        
        for c in range(COLS):
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,COLS-1,atl,heights[r][COLS-1])
        
        return list(pac & atl)



