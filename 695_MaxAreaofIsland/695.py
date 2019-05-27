'''自己的代码'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        max_area = 0
        tmp_area = 0
        def DFS(grid,i,j):
            if (i in range(row) and j in range(col) and grid[i][j]):
                grid[i][j]=0
                return 1+DFS(grid,i-1,j)+DFS(grid,i,j-1)+DFS(grid,i+1,j)+DFS(grid,i,j+1)
            return 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    continue
                
                tmp_area = DFS(grid,i,j)
                if tmp_area > max_area:
                    max_area = tmp_area
        
        return max_area

'''优秀代码'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        import queue
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        self.ans = 0
        self.grid = grid
        self.a = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.a = 0
                    self.DFS(i,j)
                    if self.a > self.ans: self.ans = self.a
        
        return self.ans
    
    def DFS(self, i, j):
        self.grid[i][j] = 0
        self.a += 1
        if i > 0 and self.grid[i-1][j] == 1:
            self.DFS(i-1,j)
        if i < len(self.grid)-1 and self.grid[i+1][j] == 1:
            self.DFS(i+1,j)
        if j > 0 and self.grid[i][j-1] == 1:
            self.DFS(i,j-1)
        if j < len(self.grid[0])-1 and self.grid[i][j+1] == 1:
            self.DFS(i,j+1)