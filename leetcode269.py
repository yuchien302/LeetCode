class Solution(object):
    
    def dfs(self, ch, dict, visit, res):
        if visit[ch] == 1:
            return False
            
        visit[ch] = 1
        nexts = dict[ch]
        for n in nexts:
            if n in visit:
                if not self.dfs(n, dict, visit, res):
                    return False
                    
        res.append(ch)
        return True
    
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        dict = {}
        visit = {}
        nodes = set()
        for w in words:
            nodes |= set(w)
        
        for c in nodes:
            dict[c] = []
            visit[c] = 0
            
        for i in range(1, len(words)):
            for (s1, s2) in zip(words[i-1], words[i]):
                if s1 != s2:
                    dict[s1].append(s2)
                    break

        res = []
        stack = []
        while len(visit) != 0:
            
            ch = list(visit.keys())[0]

            if not self.dfs(ch, dict, visit, res):
                return ""
                

            for (k, n) in visit.items():
                if n == 1:
                    visit.pop(k)

        return ''.join(reversed(res))