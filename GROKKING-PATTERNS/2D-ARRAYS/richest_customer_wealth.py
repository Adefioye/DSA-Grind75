accounts1 = [[1,2,3],[3,2,1]]
# Output: 6
accounts2 = [[1,5],[7,3],[3,5]]
# Output: 10
accounts3 = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17

# More optimal solution time = O(m)

def maximumWealth(accounts):

    maxWealth = 0 

    for amount in accounts:
        curAmount = sum(amount)
        maxWealth = max(maxWealth, curAmount) 

    return maxWealth

print(maximumWealth(accounts1))
print(maximumWealth(accounts2))
print(maximumWealth(accounts3))
# Less optimal solution time = O(m * n) 
# def maximum_wealth(accounts):
        
#     rows, cols = len(accounts), len(accounts[0])
#     max_wealth = float("-inf")
        
#     for r in range(rows):
#         cur_wealth = 0
#         for c in range(cols):
#             cur_wealth += accounts[r][c]
                
#         max_wealth = max(cur_wealth, max_wealth)
            
#     return max_wealth

# print(maximum_wealth(accounts1))
# print(maximum_wealth(accounts2))
# print(maximum_wealth(accounts3))