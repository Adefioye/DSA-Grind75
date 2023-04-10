nums1 = [1,2,1,3,2,5]
# Output: [3,5] [5, 3] is also a valid answer.
nums2 = [-1,0]
# Output: [-1,0]
nums3 = [0,1]
# Output: [1,0]

def singleNumbers(nums):

    XOR = 0 

    for num in nums:
        XOR ^= num 
    
    # Find the index of the XOR
    # Useful for partitioning nums into 2
    # Elements with or without set bit at index
    index = 0 

    while XOR:

        if XOR & 1:
            break 
        
        index += 1 
        XOR >>= 1

    # XOR1 gets XORs of nums with set bit at index 
    # XOR2 gets XORS of nums with no set bit at index
    XOR1, XOR2 = 0, 0 

    for num in nums:

        if num & (1 << index):
            XOR1 ^= num 
        else:
            XOR2 ^= num 

    return [XOR1, XOR2]

print(singleNumbers(nums1))
print(singleNumbers(nums2))
print(singleNumbers(nums3))