class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
            
        colors = len(costs[0])
        
        
        for r in range(1, len(costs)):
            for k in range(len(costs[0])):
                mincost = 1000000000
                for k_next in range(len(costs[0])):
                    if k == k_next:
                        continue
                    else:
                        mincost = min(mincost, costs[r-1][k_next])
                        
                costs[r][k] += mincost
        print(costs)
        return min(costs[-1])        