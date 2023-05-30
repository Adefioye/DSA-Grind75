def maxProfit(prices) -> int:
    left, profit = 0, 0

    for right in range(1, len(prices)):
        if prices[left] < prices[right]:
            profit = max(prices[right] - prices[left], profit)
        else:
            left = right 
        
    return profit