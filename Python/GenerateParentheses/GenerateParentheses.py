class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        list = []
        self.generateParenthDFS(list,0, 0 ,'', n)
        return list
    def generateParenthDFS(self,list, left, right, str, n):
        if right == n:
            list.append(str)
            return
        if (left < n): 
            self.generateParenthDFS(list, left+1, right, str+'(', n)
        if (right < left):
            self.generateParenthDFS(list, left, right+1, str+')', n)
            
        