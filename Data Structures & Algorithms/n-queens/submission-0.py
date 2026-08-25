class Solution:
    N = None
    result = None

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.N = n
        self.result = []
        self.backtrack(set(), set())

        output = []
        for item in self.result:
            outputItem = [['.' for i in range(n)] for i in range(n)]
            for box in item:
                row, col = self.getNthId(box)
                outputItem[row][col] = 'Q'
            output.append(outputItem)

        return [[''.join(x) for x in item] for item in output]

    def backtrack(self, currentQueens, exclusionBoxSet):
        numQueens = len(currentQueens)
        nextValidBox = []

        if numQueens == self.N:
            self.result.append(currentQueens)
            return
        else:
            nextValidBox = {(numQueens * self.N) + i for i in range(self.N)}
            nextValidBox = nextValidBox.difference(exclusionBoxSet)

        for nextBox in nextValidBox:
            self.backtrack(currentQueens.union({nextBox}), exclusionBoxSet.union(self.getRelatedBoxes(nextBox)))

    def getNthId(self, boxId):
        return (boxId // self.N, boxId % self.N)

    def getBoxId(self, rowTh, colTh):
        return (self.N * rowTh) + colTh

    def getRelatedBoxes(self, boxId):
        rowTh, colTh = self.getNthId(boxId)
        boxSet = set()
        boxSet.add(self.getBoxId(rowTh, colTh))

        idx = 0
        while idx < self.N:
            if colTh - idx >= 0:
                boxSet.add(self.getBoxId(rowTh, colTh - idx))
            
            if colTh + idx < self.N:
                boxSet.add(self.getBoxId(rowTh, colTh + idx))

            if rowTh - idx >= 0:
                boxSet.add(self.getBoxId(rowTh - idx, colTh))

            if rowTh + idx < self.N:
                boxSet.add(self.getBoxId(rowTh + idx, colTh))

            if rowTh - idx >= 0 and colTh - idx >= 0:
                boxSet.add(self.getBoxId(rowTh - idx, colTh - idx))

            if rowTh - idx >= 0 and colTh + idx < self.N:
                boxSet.add(self.getBoxId(rowTh - idx, colTh + idx))

            if rowTh + idx < self.N and colTh - idx >= 0:
                boxSet.add(self.getBoxId(rowTh + idx, colTh - idx))

            if rowTh + idx < self.N and colTh + idx < self.N:
                boxSet.add(self.getBoxId(rowTh + idx, colTh + idx))
            idx += 1
        
        return boxSet
