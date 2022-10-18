class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        
        begin, end = 0, len(height)-1
        bigContainer = 0
        
        while begin<end:
            
            bigContainer = max(bigContainer, min(height[begin],height[end])*(end-begin))
            
            if height[begin] < height[end]:
                begin += 1
                
            else:
                end -= 1
                
        return bigContainer
                