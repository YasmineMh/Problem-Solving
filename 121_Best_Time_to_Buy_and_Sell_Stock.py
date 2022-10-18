class Solution:
    
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit_ = 0
        
        begin = 0
        for end in range(1,len(prices)):
            if prices[end]<prices[begin]:
                begin = end
            maxProfit_ = max(maxProfit_, prices[end]-prices[begin])
            
        return maxProfit_