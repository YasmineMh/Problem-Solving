class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #convert the nums list to a set
        nums_set = set(nums)
        
        longest = 0
        
        for i in nums:
            
            if i-1 in nums_set:
                continue
                
            length = 1
            
            while i+length in nums_set:
                length += 1
                
            
            longest = max(longest,length)
            
        return longest