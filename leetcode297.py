class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node, res):
            if node:
                res.append(str(node.val))
                preorder(node.left, res)
                preorder(node.right, res)
            else:
                res.append('#')
            
        nodes = []
        preorder(root, nodes)
        return ','.join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def preorder(data):
            node = TreeNode(data.pop(0))
            if node.val != "#":
                node.left = preorder(data)
                node.right = preorder(data)
            else:
                return None
                
            return node

            
        data = data.split(',')
        return preorder(data)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))