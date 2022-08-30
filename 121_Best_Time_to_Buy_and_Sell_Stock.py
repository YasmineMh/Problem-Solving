class Solution:
    
    #Runtime: 1400 ms, faster than 68.50% of Python3 online submissions for Best Time to Buy and Sell Stock.
    #Memory Usage: 25 MB, less than 38.41% of Python3 online submissions for Best Time to Buy and Sell Stock.
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit_ = 0
        
        begin = 0
        for end in range(1,len(prices)):
            if prices[end]<prices[begin]:
                begin = end
            maxProfit_ = max(maxProfit_, prices[end]-prices[begin])
            
        return maxProfit_