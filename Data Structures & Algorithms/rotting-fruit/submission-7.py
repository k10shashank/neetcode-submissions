class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])

        queue = set()
        nextQueue = set()
        exclusionSet = set()
        freshFruits = set()
        time = -1

        for row in range(nRows):
            for col in range(nCols):
                if grid[row][col] == 2:
                    queue.add((row, col))
                elif grid[row][col] == 1:
                    freshFruits.add((row, col))

        if len(queue) == 0 and len(freshFruits) == 0:
            return 0
        elif len(queue) == 0 and len(freshFruits) != 0:
            return -1
        elif len(queue) != 0 and len(freshFruits) == 0:
            return 0

        while len(queue) > 0:
            for item in queue:
                row, col = item

                if row + 1 < nRows and grid[row + 1][col] != 0 and (row + 1, col) not in exclusionSet and (row + 1, col) not in queue:
                    nextQueue.add((row + 1, col))
                if row - 1 >= 0 and grid[row - 1][col] != 0 and (row - 1, col) not in exclusionSet and (row - 1, col) not in queue:
                    nextQueue.add((row - 1, col))
                if col + 1 < nCols and grid[row][col + 1] != 0 and (row, col + 1) not in exclusionSet and (row, col + 1) not in queue:
                    nextQueue.add((row, col + 1))
                if col - 1 >= 0 and grid[row][col - 1] != 0 and (row, col - 1) not in exclusionSet and (row, col - 1) not in queue:
                    nextQueue.add((row, col - 1))

                exclusionSet.add((row, col))
                freshFruits = freshFruits.difference(exclusionSet)
                grid[row][col] = 2

            time += 1
            queue, nextQueue = nextQueue, set()

        return time if len(freshFruits) == 0 else -1