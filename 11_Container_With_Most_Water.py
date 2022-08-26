class Solution:
    
    #Runtime: 802 ms, faster than 89.77% of Python3 online submissions for Container With Most Water.
    #Memory Usage: 27.3 MB, less than 85.10% of Python3 online submissions for Container With Most Water.
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
                