class Solution:
    def TrappingRainWater(self, nums):
        sum, left, right =0, 0, len(nums)-1
        left_max, right_max = nums[left], nums[right]
        while left < right:
            left_max, right_max = max(nums[left], left_max), max(nums[right], right_max)
            if left_max <= right_max:
                sum += left_max - nums[left]
                left += 1
            else:
                sum += right_max - nums[right]
                right -= 1
        return sum