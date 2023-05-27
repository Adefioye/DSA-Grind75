digits1 = [1,2,3]
# Output: [1,2,4]
digits2 = [4,3,2,1]
# Output: [4,3,2,2]
digits3 = [9]
# Output: [1,0]

# time = O(n) space = O(1)
def plusOne(nums):

    nums[-1] += 1

    for i in reversed(range(1, len(nums))):

        if nums[i] != 10:
            break 

        nums[i] = 0 
        nums[i - 1] += 1

    if nums[0] == 10:
        nums[0] = 1 
        nums.append(0)

    return nums

print(plusOne(digits1))
print(plusOne(digits2))
print(plusOne(digits3))