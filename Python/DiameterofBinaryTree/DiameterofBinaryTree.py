# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.deep(root.left)+self.deep(root.right),
                   max(self.diameterOfBinaryTree(root.left),
                   self.diameterOfBinaryTree(root.right)))   
                   
    def deep(self, root):
        if root is None:
            return 0
        return max(self.deep(root.left), self.deep(root.right))+1