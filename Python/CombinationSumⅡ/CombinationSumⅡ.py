class Solution:
    def combinationSumⅡ(nums, target):
		nums.sort()
		res=[]
		bfs(nums, target, 0, [], res)
		return res

	def bfs(nums, target, index, path, res):
		if target < 0:
			return
		if target == 0:
			res.append(path)
			return
		for i in range(index, len(nums)):
			if i > index and nums[i] == nums[i - 1]:
				continue
			if nums[i] > target:
				break
			bfs(nums, target-nums[i], i+1, path+[nums[i]], res)