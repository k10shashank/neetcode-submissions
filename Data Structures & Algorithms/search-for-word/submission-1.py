class Solution:
    nCols = None
    nRows = None
    checkWord = None
    board = None
    result = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.nRows = len(board)
        self.nCols = len(board[0])
        self.checkWord = word
        self.board = board

        for rowTh in range(self.nRows):
            for colTh in range(self.nCols):
                if not self.result:
                    self.backtrack('', {}, rowTh, colTh)
        return self.result
    
    def backtrack(self, currWord, boxIdUsed, rowTh, colTh):
        if self.result:
            return

        if currWord == self.checkWord:
            self.result = True
            return
        
        if len(currWord) > len(self.checkWord):
            return

        if rowTh < 0 or colTh < 0 or rowTh >= self.nRows or colTh >= self.nCols:
            return

        if self.checkWord[len(currWord)] != self.board[rowTh][colTh]:
            return
        
        boxId = self.getBoxId(rowTh, colTh)
        if boxId in boxIdUsed:
            return

        newBoxIdUsed = boxIdUsed.copy()
        newBoxIdUsed[boxId] = 1
        
        self.backtrack(currWord + self.board[rowTh][colTh], newBoxIdUsed, rowTh - 1, colTh)
        self.backtrack(currWord + self.board[rowTh][colTh], newBoxIdUsed, rowTh + 1, colTh)
        self.backtrack(currWord + self.board[rowTh][colTh], newBoxIdUsed, rowTh, colTh - 1)
        self.backtrack(currWord + self.board[rowTh][colTh], newBoxIdUsed, rowTh, colTh + 1)

    def getBoxId(self, rowTh, colTh):
        return (rowTh * self.nCols) + colTh