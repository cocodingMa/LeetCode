class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        res = 0
        for i in nums:
            res = res ^ i # 按位异或运算符
        return res