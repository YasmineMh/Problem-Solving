class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        combination = ""
        
        def backtracking(openP, closeP):
            nonlocal combination
            
            if openP == closeP == n:
                result.append(combination)
                return 
            
            if openP < n:
                combination += "("
                backtracking(openP+1, closeP)
                combination = combination[:-1]
                
            if closeP < openP:
                combination += ")"
                backtracking(openP, closeP+1)
                combination = combination[:-1]
                
        backtracking(0, 0)
        
        return result