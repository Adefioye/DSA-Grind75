import collections

def minWindow(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        minW = float("inf")
        left = 0
        remainingCharToCover = len(t)
        tMap = collections.Counter(t)
        startAndEnd = [-1, -1]

        # Interate through all chars in s to get the valid window and compute
        # min window with all t chars
        for right in range(len(s)):
            rightChar = s[right]

            # if char in tMap, decrement value and remainingCharToCover 
            if rightChar in tMap:
                tMap[rightChar] -= 1
                if tMap[rightChar] >= 0:
                    remainingCharToCover -= 1

            # Check if there is a valid window
            while remainingCharToCover == 0:
                if (right - left + 1) < minW:
                    minW = right - left + 1
                    startAndEnd = [left, right]

                leftChar = s[left]

                if leftChar in tMap:
                    tMap[leftChar] += 1
                    if tMap[leftChar] > 0:
                        remainingCharToCover += 1
                
                left += 1
                
        x, y = startAndEnd
        return s[x : y + 1] if minW != float("inf") else ""