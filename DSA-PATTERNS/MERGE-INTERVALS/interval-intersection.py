firstList1 = [[0,2],[5,10],[13,23],[24,25]]
secondList1 = [[1,5],[8,12],[15,24],[25,26]]
# [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

firstList2 = [[1,3],[5,9]]
secondList2 = []
# []

def intervalIntersection(firstList, secondList):

    p1 = 0
    p2 = 0
    res = []

    while p1 < len(firstList) and p2 < len(secondList):
            
        s1, e1 = firstList[p1]
        s2, e2 = secondList[p2]

        if e2 >= s1 and e1 >= s2:
            res.append([max(s1, s2), min(e1, e2)])

        if e1 <= e2:
            p1 += 1
        else:
            p2 += 1

    return res

print(intervalIntersection(firstList1, secondList1))
print(intervalIntersection(firstList2, secondList2))