class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nRows = len(heights)
        nCols = len(heights[0])

        atlanticSet = set()
        pacificSet = set()

        queue = {(0, i) for i in range(0, nCols)}.union((i, 0) for i in range(nRows))
        nextQueue = set()

        while len(queue) > 0:
            for item in queue:
                pacificSet.add(item)
                row, col = item

                if row - 1 >= 0 and heights[row - 1][col] >= heights[row][col] and (row - 1, col) not in queue and (row - 1, col) not in pacificSet:
                    nextQueue.add((row - 1, col))

                if row + 1 < nRows and heights[row + 1][col] >= heights[row][col] and (row + 1, col) not in queue and (row + 1, col) not in pacificSet:
                    nextQueue.add((row + 1, col))

                if col - 1 >= 0 and heights[row][col - 1] >= heights[row][col] and (row, col - 1) not in queue and (row, col - 1) not in pacificSet:
                    nextQueue.add((row, col - 1))

                if col + 1 < nCols and heights[row][col + 1] >= heights[row][col] and (row, col + 1) not in queue and (row, col + 1) not in pacificSet:
                    nextQueue.add((row, col + 1))

            queue, nextQueue = nextQueue, set()


        queue = {(nRows - 1, i) for i in range(0, nCols)}.union((i, nCols - 1) for i in range(nRows))
        nextQueue = set()

        while len(queue) > 0:
            for item in queue:
                atlanticSet.add(item)
                row, col = item

                if row - 1 >= 0 and heights[row - 1][col] >= heights[row][col] and (row - 1, col) not in queue and (row - 1, col) not in atlanticSet:
                    nextQueue.add((row - 1, col))

                if row + 1 < nRows and heights[row + 1][col] >= heights[row][col] and (row + 1, col) not in queue and (row + 1, col) not in atlanticSet:
                    nextQueue.add((row + 1, col))

                if col - 1 >= 0 and heights[row][col - 1] >= heights[row][col] and (row, col - 1) not in queue and (row, col - 1) not in atlanticSet:
                    nextQueue.add((row, col - 1))

                if col + 1 < nCols and heights[row][col + 1] >= heights[row][col] and (row, col + 1) not in queue and (row, col + 1) not in atlanticSet:
                    nextQueue.add((row, col + 1))

            queue, nextQueue = nextQueue, set()

        return [[item[0], item[1]] for item in pacificSet.intersection(atlanticSet)]