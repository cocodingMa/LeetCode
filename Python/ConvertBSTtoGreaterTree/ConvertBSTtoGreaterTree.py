# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sum = 0 # 注意sum的初始化位置
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
			return 
        self.convertBST(root.right)
        root.val += self.sum
        self.sum = root.val
        self.convertBST(root.left)
        return root
        