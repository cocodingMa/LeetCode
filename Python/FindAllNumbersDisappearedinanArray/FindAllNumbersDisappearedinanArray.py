# 解法一
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                self.swap(i, nums[i]-1, nums)
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(i+1)
        return res
    
    def swap(self, i, j, nums):
        nums[i], nums[j] = nums[j], nums[i]
        return nums
		
		
#解法二	
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
			if nums[abs(nums[i])-1] > 0:
				nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
				
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res