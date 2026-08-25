class Solution:
    exclusionBoxSet = None
    grid = None
    nRows = None
    nCols = None
    result = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        self.exclusionBoxSet = set()
        self.grid = grid
        self.nRows = len(grid)
        self.nCols = len(grid[0])
        self.result = 0
        
        for rowTh in range(self.nRows):
            for colTh in range(self.nCols):
                if self.grid[rowTh][colTh] == '1' and (rowTh, colTh) not in self.exclusionBoxSet:
                    self.backtrack(rowTh, colTh)
                    self.result += 1
        
        return self.result

    def backtrack(self, rowTh, colTh):
        if rowTh < 0 or colTh < 0 or rowTh >= self.nRows or colTh >= self.nCols:
            return
        
        if self.grid[rowTh][colTh] == '0':
            return

        if (rowTh, colTh) in self.exclusionBoxSet:
            return
        
        self.exclusionBoxSet.add((rowTh, colTh))
        
        self.backtrack(rowTh - 1, colTh)
        self.backtrack(rowTh + 1, colTh)
        self.backtrack(rowTh, colTh - 1)
        self.backtrack(rowTh, colTh + 1)