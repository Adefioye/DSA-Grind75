intervals1 = [[1,3],[6,9]]; newInterval1 = [2,5]    #   [[1,5],[6,9]]
intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]; newInterval2 = [4,8]   #   [[1,2],[3,10],[12,16]]


def insert(intervals, newInterval):

    output = []

    for i, interval in enumerate(intervals):

        s1, e1 = interval 
        s2, e2 = newInterval

        if s2 <= e1 and e2 >= s1:
            # Merge
            newInterval = [min(s1, s2), max(e1, e2)]
        else:
            # Add new interval or
            # Add current interval
            if s2 < s1:
                output.append(newInterval)
                return output + intervals[i:]
            else:
                output.append(interval)
    
    # In case there is no insertion of new interval
    output.append(newInterval)

    return output


print(insert(intervals1, newInterval1))
print(insert(intervals2, newInterval2))

# def insert(intervals, newInterval):
#     res = []

#     for i, interval in enumerate(intervals):
#         # Check if end of new interval is less than start of current interval
#         # Check if start of new interval is greater than end of current interval
#         # Merge if conditions above are false

#         if newInterval[1] < interval[0]:
#             res.append(newInterval)
#             return res + intervals[i:]
#         elif newInterval[0] > interval[1]:
#             res.append(interval)
#         else:
#             newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

#     res.append(newInterval)
        
#     return res















# class Solution:
#     def insert(intervals, newInterval):

#         if len(intervals) == 0:
#             return [newInterval]

#         if len(intervals) == 1:

#             start, end = newInterval
#             if start <= intervals[-1][-1]:
#                 intervals[-1][-1] = max(intervals[-1][-1], end)
#             else:
#                 intervals.append([start, end])

#             return intervals

#         stack = [intervals[0]]
#         nextPointer = 1

#         startNewInterval, endNewInterval = newInterval

#         if startNewInterval <= stack[-1][-1]:
#             #Merge new interval
#             stack[-1][-1] = max(stack[-1][-1], endNewInterval)
#         else:

#             while nextPointer < len(intervals):
#                 nextInterval = intervals[nextPointer]
#                 startNextInterval, endNextInterval = nextInterval
                
#                 # Try and determine whether to append nextInterval / newInterval
#                 if startNextInterval < startNewInterval:
#                     # Try and merge next interval

#                     if startNextInterval <= stack[-1][-1]:
#                         #Merge next interval
#                         stack[-1][-1] = max(stack[-1][-1], endNextInterval)
#                     else:
#                         stack.append(nextInterval)
#                         nextPointer += 1
#                 else:

#                     # Try and merge newInterval

#                     if startNewInterval <= stack[-1][-1]:
#                         stack[-1][-1] = max(stack[-1][-1], endNewInterval)
#                     else:
#                         stack.append(newInterval)

#                     break

        
#         while nextPointer < len(intervals):
#             start, end = intervals[nextPointer]

#             if start <= stack[-1][-1]:
#                 stack[-1][-1] = max(stack[-1][-1], end)
#             else:
#                 stack.append([start, end])
            
#             nextPointer += 1

        
#         return stack