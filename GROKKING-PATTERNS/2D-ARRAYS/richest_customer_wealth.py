from typing import List 

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        rows, cols = len(accounts), len(accounts[0])
        max_wealth = float("-inf")
        
        for r in range(rows):
            cur_wealth = 0
            for c in range(cols):
                cur_wealth += accounts[r][c]
                
            max_wealth = max(cur_wealth, max_wealth)
            
        return max_wealth