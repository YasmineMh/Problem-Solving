class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_stock = {}
        
        for index,i in enumerate(nums):
            diff = target - i
            if diff in dict_stock:
                return [dict_stock[diff],index]
            dict_stock[i] = index