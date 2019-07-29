class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n, beg, end,= len(nums), -1, -2
        maxRes ,minRes = nums[0], nums[n-1]
        for i in range(1,len(nums)):
            maxRes = max(maxRes, nums[i])
            minRes = min(minRes, nums[n-1-i])
            if nums[i] < maxRes :
                end = i
            if nums[n-1-i] > minRes :
                beg = n-1-i
        return end - beg + 1