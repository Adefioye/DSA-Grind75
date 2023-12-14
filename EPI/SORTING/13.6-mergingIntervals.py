class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []

        for i, interval in enumerate(intervals):
            s1, e1 = interval
            s2, e2 = newInterval

            if s1 <= e2 and s2 <= e1:
                # overlap exists, so create newInterval
                newInterval = [min(s1, s2), max(e1, e2)]
            else:
                # Either insert current interval or newInterval
                if e1 < e2:
                    # Add current interval
                    res.append(interval)
                else:
                    # Add current interval
                    res.append(newInterval)
                    res.extend(intervals[i:])
                    return res

        # Add newInterval, since not added yet
        res.append(newInterval)
        return res
        