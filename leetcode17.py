class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        pad = {}
        pad["0"] = ""
        pad["1"] = ""
        pad["2"] = "abc"
        pad["3"] = "def"
        pad["4"] = "ghi"
        pad["5"] = "jkl"
        pad["6"] = "mno"
        pad["7"] = "pqrs"
        pad["8"] = "tuv"
        pad["9"] = "wxyz"
        
        return reduce(lambda acc, digit: [ a + d for a in acc for d in digit], map(pad.get, digits), [""])
            