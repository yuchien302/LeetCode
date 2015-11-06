class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
            
        for c in range(1, len(costs)):
            costs[c][0] += min(costs[c-1][1], costs[c-1][2])
            costs[c][1] += min(costs[c-1][0], costs[c-1][2])
            costs[c][2] += min(costs[c-1][0], costs[c-1][1])
            
        return min(costs[-1])