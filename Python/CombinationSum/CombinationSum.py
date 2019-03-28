class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.dfs(candidates, target, 0, [], result)
        return result
    
    def dfs(self, list, target, index, path, result):
        if target < 0:
            return
        if target == 0:
            result.append(path)
            return
        for i in range(index, len(list)):
            self.dfs(list, target-list[i], i, path+[list[i]], result)