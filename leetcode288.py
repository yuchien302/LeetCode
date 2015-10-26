from collections import defaultdict
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = defaultdict(set)

        for word in dictionary:
            abbr = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
            self.dict[abbr].add(word)

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = word if len(word) <= 2 else word[0] + str(len(word)-2) + word[-1]
        
        return ((len(self.dict[abbr]) == 0) or 
                (len(self.dict[abbr]) == 1 and word in self.dict[abbr]))
            
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")