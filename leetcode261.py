class Solution(object):
    
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        def dfs(i):
            map(dfs, graph.pop(i, []))
                
        if n != len(edges) + 1:
            return False
        
        graph = { i: [] for i in range(n) }
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
            
        dfs(0)
        return len(graph) == 0
        
        