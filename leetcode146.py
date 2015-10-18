from collections import OrderedDict


class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = OrderedDict()
        self.cap = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dict:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value
            return self.dict[key]
        return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            del self.dict[key]
            
        self.dict[key] = value
        if len(self.dict) > self.cap:
            self.dict.popitem(last=False)
        
        