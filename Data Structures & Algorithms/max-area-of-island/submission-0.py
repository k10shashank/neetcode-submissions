class Solution:
    exclusionBoxSet = None
    grid = None
    nRows = None
    nCols = None
    result = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.exclusionBoxSet = set()
        self.grid = grid
        self.nRows = len(grid)
        self.nCols = len(grid[0])
        self.result = 0
        
        for rowTh in range(self.nRows):
            for colTh in range(self.nCols):
                if self.grid[rowTh][colTh] == 1 and (rowTh, colTh) not in self.exclusionBoxSet:
                    self.result = max(self.result, self.backtrack(rowTh, colTh))
        
        return self.result

    def backtrack(self, rowTh, colTh):
        if rowTh < 0 or colTh < 0 or rowTh >= self.nRows or colTh >= self.nCols:
            return 0
        
        if self.grid[rowTh][colTh] == 0:
            return 0

        if (rowTh, colTh) in self.exclusionBoxSet:
            return 0
        
        self.exclusionBoxSet.add((rowTh, colTh))

        return 1 + self.backtrack(rowTh - 1, colTh) + self.backtrack(rowTh + 1, colTh) + self.backtrack(rowTh, colTh - 1) + self.backtrack(rowTh, colTh + 1)