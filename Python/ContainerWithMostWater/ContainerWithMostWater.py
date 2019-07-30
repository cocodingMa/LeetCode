class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = left =0
        right = len(height)-1
        while right > left:
            maxWater = max(min(height[right], height[left])*(right-left), maxWater)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return maxWater
    
        
        