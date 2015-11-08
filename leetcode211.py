class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.val = ""
        self.is_word = False
        
        
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
                node.child[c].val = c
            node = node.child[c]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def search_helper(word, node):
            for i, c in enumerate(word):
                if c == '.':
                    return any([search_helper(word[i+1:], child) for child in node.child.values()])
                    
                elif c not in node.child:
                    return False
                node = node.child[c]
            return node.is_word
        return search_helper(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")