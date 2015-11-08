import re
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = re.sub("//+", "/", path)
        paths = path.split('/')
        paths = [p for p in paths if p not in ['', '.']]
        i = 0
        # print(paths)
        while i< len(paths):
            if i >= 0 and paths[i] == "..":
                paths.pop(i)
                if i>0:
                    paths.pop(i-1)
                i -= 1
                continue
            i += 1
            
        return '/' + '/'.join(paths)
        