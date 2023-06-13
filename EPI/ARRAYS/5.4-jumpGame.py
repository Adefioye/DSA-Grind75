prices1 = [2,3,1,1,4]
# Output: True
prices2 = [3,2,1,0,4]
# Output: False


def canJump(nums) -> bool:

    reachability = 0

    for i in range(len(nums)):

        if reachability < i:
            return False 

        reachability = max(reachability, i + nums[i])

    return True

print(canJump(prices1))
print(canJump(prices2))