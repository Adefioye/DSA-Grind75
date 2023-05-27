nums1 = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
nums2 = [2,0,1]
# Output: [0,1,2]

# 2 PASS SOLUTION
# time = O(n), space = O(1)
def dutchNationalFlap2Pass(nums):
    l, r = 0, len(nums) - 1 
    PIVOT = 1

    for i in range(len(nums)):

        if nums[i] < PIVOT:
            # Swap and increment l 
            nums[i], nums[l] = nums[l], nums[i]
            l += 1 

    for i in range(len(nums) - 1, -1, -1):

        if i < l:
            break 

        if nums[i] > PIVOT:
            # Swap and decrement r
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1 

    return nums


# print(dutchNationalFlap2Pass(nums1))
# print(dutchNationalFlap2Pass(nums2))

def dutchNationalFlag1Pass(nums):

    # This depends on 3 groups
    # smaller --> nums[:smaller] < pivot
    # equal   --> nums[smaller:equal]
    # unclassified --> nums[equal:larger]
    # larger       --> nums[larger:]
    smaller, equal, larger = 0, 0, len(nums)
    PIVOT = 1

    while equal < larger:

        if nums[equal] < PIVOT:
            nums[equal], nums[smaller] = nums[smaller], nums[equal]
            smaller += 1
            equal += 1 
        elif nums[equal] == PIVOT:
            equal += 1 
        else:
            larger -= 1 
            nums[equal], nums[larger] = nums[larger], nums[equal]

    return nums 

print(dutchNationalFlag1Pass(nums1))
print(dutchNationalFlag1Pass(nums2))
