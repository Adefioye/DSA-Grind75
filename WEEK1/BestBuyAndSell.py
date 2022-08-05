class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        left = 0
        right = 1
        
        while right < len(prices):
            
            if prices[left] < prices[right]:
                cur_profit = prices[right] - prices[left]
                max_profit = max(cur_profit, max_profit)
            else:
                left = right
                
            right += 1
                
        return max_profit