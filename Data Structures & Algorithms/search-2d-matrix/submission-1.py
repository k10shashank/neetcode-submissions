class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            i_row = mid // cols
            i_col = mid - (i_row * cols)

            if target < matrix[i_row][i_col]:
                high = mid - 1
            elif target > matrix[i_row][i_col]:
                low = mid + 1
            else:
                return True
        
        return False
 