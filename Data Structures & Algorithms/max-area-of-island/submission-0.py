class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        result=0
        seen=set()

        rows=len(grid)
        cols=len(grid[0])

        def dfs(r,c):
            if (r,c) in seen:
                return 0
            if r>=rows or r<0 or c>=cols or c<0:
                return 0
            if grid[r][c]!=1:
                return 0
            
            area=1
            seen.add((r,c))

            for dr,dc in directions:
                area+=dfs(r+dr,c+dc)
        
            return area
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c]==1:
                    result=max(result, dfs(r,c))
        return result