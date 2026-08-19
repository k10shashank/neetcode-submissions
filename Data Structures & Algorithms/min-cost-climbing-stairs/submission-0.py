class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = []
        N = len(cost)
        for idx in range(N):
            if idx == 0 or idx == 1:
                minCost.append(cost[idx])
            else:
                minCost.append(min(minCost[idx-1], minCost[idx-2]) + cost[idx])
        
        return min(minCost[N-1], minCost[N-2])
        