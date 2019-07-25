class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = cur = 0
        for i in nums:
            temp = max(pre+i, cur)
            pre = cur
            cur = temp
        return cur