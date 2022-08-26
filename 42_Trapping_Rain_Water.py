class Solution:
    
    #Runtime: 136 ms, faster than 89.94% of Python3 online submissions for Trapping Rain Water.
    #Memory Usage: 16.1 MB, less than 45.17% of Python3 online submissions for Trapping Rain Water.
    def trap(self, height: List[int]) -> int:
        
        begin, end = 0, len(height)-1
        maxBegin, maxEnd = height[begin], height[end]
        waterTrapped = 0
        
        while begin<end:
            
            if height[begin]<height[end]:
                begin += 1
                maxBegin = max(maxBegin, height[begin])
                waterTrapped += maxBegin-height[begin]
                
            else:
                end -= 1
                maxEnd = max(maxEnd, height[end])
                waterTrapped += maxEnd-height[end]
                
        return waterTrapped