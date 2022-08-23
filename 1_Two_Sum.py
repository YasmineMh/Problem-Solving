class Solution:
    
    #Runtime: 62 ms, faster than 95.87% of Python3 online submissions for Two Sum.
    #Memory Usage: 15.1 MB, less than 50.22% of Python3 online submissions for Two Sum.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_stock = {}
        
        for index,i in enumerate(nums):
            diff = target - i
            if diff in dict_stock:
                return [dict_stock[diff],index]
            dict_stock[i] = index