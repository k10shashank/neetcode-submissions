class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [None for i in range(amount + 1)]
        arr[0] = 0

        
        for i in range(1, amount + 1):
            minval = None
            for cn in coins:
                if i - cn >= 0:
                    minval = minNone(arr[i-cn], minval)
            arr[i] = minval + 1 if minval is not None else None
        
        return arr[amount] if arr[amount] is not None else -1


def minNone(a, b):
    if b is None and a is None:
        return None
    elif b is None:
        return a
    elif a is None:
        return b
    else:
        return min(a,b)
