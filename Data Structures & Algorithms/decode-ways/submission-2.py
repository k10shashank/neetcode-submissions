class Solution:
    def numDecodings(self, s: str) -> int:
        fibo, N = [], len(s)
        for i in range(1 + N):
            if len(fibo) <= 1:
                fibo.append(1)
            else:
                fibo.append(fibo[-1] + fibo[-2])
        
        idx, fseq, output = 0, 0, 1
        while idx < N:
            digit  = int(s[idx])

            if digit == 0:
                if idx == 0 or fseq == 0:
                    return 0
                else:
                    output *= (fibo[fseq-1])
                    fseq= 0

            elif digit <= 2:
                fseq += 1

            elif digit <= 6:
                output *= (fibo[fseq+1])
                fseq = 0

            elif digit <= 9:
                if idx > 0 and s[idx-1] == '1':
                    output *= (fibo[fseq+1])
                    fseq = 0
                else:
                    output *= (fibo[fseq])
                    fseq = 0

            idx += 1
        
        if fseq > 0:
            output *= (fibo[fseq])
        
        return output
