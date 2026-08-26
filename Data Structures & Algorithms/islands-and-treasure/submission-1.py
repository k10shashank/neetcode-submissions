class Solution:
    grid = None
    nRows = None
    nCols = None

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.nRows = len(grid)
        self.nCols = len(grid[0])

        queue = set()
        nextQueue = set()
        exclusionSet = set()
        currDist = 0

        for rowTh in range(self.nRows):
            for colTh in range(self.nCols):
                if self.grid[rowTh][colTh] == 0:
                    queue.add((rowTh, colTh))

        while len(queue) > 0:
            for item in queue:
                rowTh, colTh = item

                if rowTh < 0 or colTh < 0 or rowTh >= self.nRows or colTh >= self.nCols or grid[rowTh][colTh] == -1 or (rowTh, colTh) in exclusionSet:
                    continue

                nextQueue.add((rowTh + 1, colTh))
                nextQueue.add((rowTh - 1, colTh))
                nextQueue.add((rowTh, colTh + 1))
                nextQueue.add((rowTh, colTh - 1))

                exclusionSet.add((rowTh, colTh))
                grid[rowTh][colTh] = currDist

            currDist += 1
            queue, nextQueue = nextQueue, set()
