nums = [2, 1, 2, 5, 6, 5, 7, 7, 6]

def singleNumber(nums):
    """
    Returns element that appears once in the unsorted array
    """
    XOR = nums[0]

    for i in range(1, len(nums)):
        XOR ^= nums[i]

    return XOR

print(singleNumber(nums))