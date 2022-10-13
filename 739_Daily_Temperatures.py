class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        output = [0] * len(temperatures)
        stack = []
        
        for index, i in enumerate(temperatures):
            
            while stack and i > stack[-1][0]:
                element_index = stack.pop()[1]
                output[element_index] = index - element_index
                
            stack.append((i, index))
        
        return output