class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.house_robber(nums[1:]), self.house_robber(nums[:-1]))
    
    def house_robber(self, nums: List[int]) -> int:
        
        house1, house2 = 0, 0
        
        for i in nums:
            highest = max(house1 + i, house2)
            house1 = house2
            house2 = highest
            
        return house2