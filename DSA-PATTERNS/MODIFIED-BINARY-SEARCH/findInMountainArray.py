class Solution:
    def findInMountainArray(self, target, mountain_arr) -> int:

        # First search peak of the mountain 
        # Find target from 0 to peak of mountain, if not
        # Find target from peak right side of mountain, if not, return -1

        peak = self.findPeak(mountain_arr)

        if mountain_arr.get(peak) == target:
            return peak
        # Search left
        minIdx = self.binarySearch(0, peak - 1, mountain_arr, target, True)

        if minIdx != -1:
            return minIdx
        
        # Not in left search right
        minIdx = self.binarySearch(peak + 1, mountain_arr.length() - 1, mountain_arr, target, False)
        if minIdx != -1:
            return minIdx

        return minIdx


    def findPeak(self, mountain):
        # Ignore extremes 1 and last since they can be answer
        l, r = 1, mountain.length() - 2 
        
        while l <= r:

            mid = (l + r) // 2 

            if mountain.get(mid - 1) < mountain.get(mid) > mountain.get(mid + 1):
                return mid 
            elif mountain.get(mid - 1) < mountain.get(mid) < mountain.get(mid + 1):
                l = mid + 1
            else:
                r = mid - 1 

    def binarySearch(self, l, r, mountain, target, isAscending):

        if isAscending:

            while l <= r:

                mid = (l + r) // 2 
                if target < mountain.get(mid):
                    r = mid - 1
                elif target > mountain.get(mid):
                    l = mid + 1 
                else:
                    return mid 
        
            return -1
        else:

            while l <= r:

                mid = (l + r) // 2 
                if target > mountain.get(mid):
                    # [5, 4, 3, 1] 
                    r = mid - 1 
                elif target < mountain.get(mid):
                    l = mid + 1 
                else:
                    return mid 

            return -1
