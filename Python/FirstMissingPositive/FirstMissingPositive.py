class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1;
        return len(nums) + 1

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]