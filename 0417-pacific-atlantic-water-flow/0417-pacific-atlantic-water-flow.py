class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        
        visited1 = [[0]*col for _ in range(row)]
        visited2 = [[0]*col for _ in range(row)]
        dy = [0, 0, 1, -1]
        dx = [1, -1, 0, 0]
        
        ans = []
        
        def DFS(y, x, visited, prev):
            if 0<=y<row and 0<=x<col and visited[y][x]==0 and heights[y][x]>=prev:
                visited[y][x] = 1
                
                for t in range(4):
                    newY, newX = y+dy[t], x+dx[t]
                    DFS(newY, newX, visited, heights[y][x])
        
        for y in range(row):
            DFS(y, 0, visited1, 0)
            DFS(y, col-1, visited2, 0)
        for x in range(col):
            DFS(0, x, visited1, 0)
            DFS(row-1, x, visited2, 0)
        
        for y in range(row):
            for x in range(col):
                if visited1[y][x]==1 and visited2[y][x]==1:
                    ans.append([y, x])
        
        return ans