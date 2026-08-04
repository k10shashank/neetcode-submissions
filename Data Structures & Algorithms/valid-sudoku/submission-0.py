class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, box = [], [], []
        for i in range(9):
            rows.append(dict())
            cols.append(dict())
            box.append(dict())

        for rowidx in range(9):
            for colidx in range(9):
                value = board[rowidx][colidx]
                if value == '.':
                    continue
                
                if rows[rowidx].get(value) is None:
                    rows[rowidx][value] = True
                else:
                    return False
                
                if cols[colidx].get(value) is None:
                    cols[colidx][value] = True
                else:
                    return False
                
                boxid = 3 * (rowidx // 3) + colidx // 3
                if box[boxid].get(value) is None:
                    box[boxid][value] = True
                else:
                    return False
        
        return True
        