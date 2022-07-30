nums = [2,7,11,15]
target = 9

def twoSum_brute(nums, target):

    for i in range(len(nums)):
        ntf = target - nums[i]

        for j in range(i + 1, len(nums)):

            if nums[j] == ntf:
                return [i, j]

def twoSum_optimal(nums, target):
    ntf_map= {}
        
    for i in range(len(nums)):
        current_num = nums[i]
        ntf = target - current_num 
            
        if current_num not in ntf_map:
            ntf_map[ntf] = i 
        else:
            return [ntf_map[current_num], i]

# print(twoSum_optimal(nums, target))
print(twoSum_brute(nums, target))