class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        for i in range( max(len(v1), len(v2)) ):
            if i == len(v1):
                v1.append(0)
            if i == len(v2):
                v2.append(0)
            
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0
                
        
     