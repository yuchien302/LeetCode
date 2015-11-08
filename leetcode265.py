class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0 or len(costs[0]) == 0:
            return 0
            
        for r in range(1, len(costs)):
            sorted_costs = sorted(costs[r-1])
            
            min_cost0 = sorted_costs[0]
            min_cost1 = sorted_costs[1]
            min_idx0 = costs[r-1].index(min_cost0)

            for k in range(len(costs[0])):

                if k == min_idx0:
                    costs[r][k] += min_cost1
                else:
                    costs[r][k] += min_cost0

        return min(costs[-1])        