class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        I, J, I_MAX, J_MAX = 0, 0, len(matrix) - 1, len(matrix[0]) - 1

        while I < I_MAX and J < J_MAX:
            for s in range(J, J_MAX):
                output.append(matrix[I][s])
            for s in range(I, I_MAX):
                output.append(matrix[s][J_MAX])
            for s in range(J_MAX, J, -1):
                output.append(matrix[I_MAX][s])
            for s in range(I_MAX, I, -1):
                output.append(matrix[s][J])
            
            I += 1
            J += 1
            I_MAX -= 1
            J_MAX -= 1

        if I < I_MAX and J == J_MAX:
            for s in range(I, I_MAX + 1):
                output.append(matrix[s][J])

        if I == I_MAX and J < J_MAX:
            for s in range(J, J_MAX + 1):
                output.append(matrix[I][s])

        if I == I_MAX and J == J_MAX:
            output.append(matrix[I][J])
        
        return output
        