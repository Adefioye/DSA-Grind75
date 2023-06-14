prices1 = [3,3,5,0,0,3,1,4]
# Output: 6
prices2 = [1,2,3,4,5]
# Output: 4

def maxProfit(prices) -> int:

    forwardBuySellProfits = [0] * len(prices)
    backwardBuySellProfits = [0] * len(prices)

    small = prices[0]
    fMaxProfitSoFar = 0
    bMaxProfitSofar = 0
    high = prices[-1]
    for i in range(1, len(prices)):

        if prices[i] > small:
            fMaxProfitSoFar = max(fMaxProfitSoFar, prices[i] - small)
            
        if prices[i] < small:
            small = prices[i]

        forwardBuySellProfits[i] = fMaxProfitSoFar

    for i in range(len(prices) - 2, -1, -1):

        if prices[i] < high:
            bMaxProfitSofar = max(bMaxProfitSofar, high - prices[i])

        if prices[i] > high:
            high = prices[i]

        backwardBuySellProfits[i] = bMaxProfitSofar

    totalBuySellProfits = [0] * len(prices)
    for i in range(len(prices)):
        if i == 0:
            totalBuySellProfits[i] = 0 + backwardBuySellProfits[i]
        else:
            totalBuySellProfits[i] = forwardBuySellProfits[i-1] + backwardBuySellProfits[i]

    return max(totalBuySellProfits)

print(maxProfit(prices1))
print(maxProfit(prices2))