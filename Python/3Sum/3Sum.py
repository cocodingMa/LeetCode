class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        listRes = []
        for i in range(len(nums)):
            left = i - 1
            right = i + 1
            while left > -1 and right < (len(nums)):
                num = nums[left] + nums[i] + nums[right]
                if num == 0:
                    listRes.append([nums[left], nums[i], nums[right]])
                    while left > -1 and nums[left] == nums[left+1]:
                        left -=1
                    while right < (len(nums)) and nums[right] == nums[right-1]:
                        right += 1
                    right += 1
                    left -= 1
                elif num < 0:
                    right += 1
                else:
                    left -= 1
        return listRes
                    