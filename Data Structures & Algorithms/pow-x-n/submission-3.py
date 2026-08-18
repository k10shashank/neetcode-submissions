class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x

        if x == -1:
            return 1 if n % 2 == 0 else -1

        output = 1.0
        if n >= 0:
            while n > 0:
                output = output * x
                n = n - 1
            return output
        else:
            while n < 0:
                output = output / x
                n = n + 1
                if output < 0.00001:
                    return 0
            return output
        