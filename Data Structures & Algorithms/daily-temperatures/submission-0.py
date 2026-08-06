class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        result = []
        for i in range(len(temperatures) - 1, -1, -1):
            cnt = 0
            while len(stk) != 0 and stk[-1][0] <= temperatures[i]:
                stk.pop()
            if len(stk) == 0:
                result.append(0)
            else:
                result.append(stk[-1][1] - i)
            stk.append((temperatures[i], i))
        arr = []
        for i in range(len(result)):
            arr.append(result.pop())
        return arr
        