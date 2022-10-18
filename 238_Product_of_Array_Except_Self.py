class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #initialize the the result list
        result_list = [1] * len(nums)
        
        #the product of prefix elements
        prefix_elemnts = 1
        for i in range(len(nums)):
            result_list[i] = prefix_elemnts
            prefix_elemnts *= nums[i]
            
        #the product of suffix elements
        suffix_elemnts = 1
        for i in range(len(nums)-1,-1,-1):
            result_list[i] *= suffix_elemnts
            suffix_elemnts *= nums[i]
            
        return result_list