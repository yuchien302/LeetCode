# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        node = root
        
        while node:
            self.nodes.append(node)
            node = node.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.nodes) != 0
        

    def next(self):
        """
        :rtype: int
        """
        
        node = self.nodes.pop()
        val = node.val
        
        node = node.right
        while node:
            self.nodes.append(node)
            node = node.left
            
        return val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())