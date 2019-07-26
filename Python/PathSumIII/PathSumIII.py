# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is	None:
			return 0
        return self.pathSum(root.left, sum)+self.pathSum(root.right, sum)+self.pathSumDFS(root, sum)
	
    def pathSumDFS(self, root, sum):
        if root is None:
            return 0
        return (1 if root.val == sum else 0) + self.pathSumDFS(root.left, sum-root.val)+ self.pathSumDFS(root.right, sum-root.val)