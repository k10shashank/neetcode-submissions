class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        I, J = 0, N-1
        while I < J:
            side = J - I
            for s in range(side):
                matrix[I][I + s], matrix[I + s][J], matrix[J][J - s], matrix[J - s][I] = matrix[J - s][I], matrix[I][I + s], matrix[I + s][J], matrix[J][J - s]

            I += 1
            J -= 1
        