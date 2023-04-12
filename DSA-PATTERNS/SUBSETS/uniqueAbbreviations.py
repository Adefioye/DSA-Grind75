s1 = "BAT"
# Output: "BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"

s2 = "code"
# "code", "cod1", "co1e", "co2", "c1de", "c1d1", "c2e", "c3", "1ode", "1od1", "1o1e", "1o2", 
# "2de", "2d1", "3e", "4"
def uniqueAbbreviations(s):
    res = []

    def addOnehelper(path):

        if len(path) == 0:
            return path + "1"
        last = path[-1]

        if not last.isdigit():
            return path + "1"
        
        rest = path[:-1]
        numToAdd = int(last) + 1
        return rest + str(numToAdd)
    
    def dfs(i, path):

        if i >= len(s):
            res.append(path)
            return

        # Decision to include s[i]
        dfs(i + 1, path + s[i])

        # Decision to add 1
        dfs(i + 1, addOnehelper(path))

    dfs(0, "")

    return res 

print(uniqueAbbreviations(s1))
print(uniqueAbbreviations(s2))

