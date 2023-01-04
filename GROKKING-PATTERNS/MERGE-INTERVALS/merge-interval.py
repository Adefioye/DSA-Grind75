intervals = [[1,3], [2,6], [15,18], [8,10]]    #   [[1,6],[8,10],[15,18]]
intervals1 = [[1,4],[4,5]]                  #   [[1,5]]


def merge(intervals):
    
    intervals.sort(key = lambda row: row[0])

    stack = [intervals[0]]

    for start, end in intervals[1:]:

        lastEnd = stack[-1][-1]
        if start <= lastEnd:
            stack[-1][-1] = max(lastEnd, end)
        else:
            stack.append([start, end])

    return stack

print(merge(intervals))
print(merge(intervals1))