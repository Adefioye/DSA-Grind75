intervals1 = [[1,2],[2,3],[3,4],[1,3]]      #   1
intervals2 = [[1,2],[1,2],[1,2]]            #   2
intervals3 = [[1,2],[2,3]]                  #   0



def eraseOverlapIntervals(intervals):

    intervals.sort(key= lambda x: x[0])
    prevEnd = intervals[0][1]
    total = 0

    for start, end in intervals[1:]:

        if start < prevEnd:
            total += 1
            prevEnd = min(end, prevEnd)
        else:
            prevEnd = end
        
    return total


print(eraseOverlapIntervals(intervals1))
print(eraseOverlapIntervals(intervals2))
print(eraseOverlapIntervals(intervals3))
        