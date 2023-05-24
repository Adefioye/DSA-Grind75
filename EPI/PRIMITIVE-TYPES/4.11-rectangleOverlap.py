
# Rectangle overlaps
# When l1 < e2 and l2 < e1
# rec = [x1, y1, x2, y2]

rec1_1 = [0,0,2,2]; rec2_1 = [1,1,3,3]
# Output: true
rec1_2 = [0,0,1,1]; rec2_2 = [1,0,2,1]
# Output: false
rec1_3 = [0,0,1,1]; rec2_3 = [2,2,3,3]
# Output: false

def rectangleOverlap(rec1, rec2):

    l1, e1 = rec1[:2], rec1[2:]
    l2, e2 = rec2[:2], rec2[2:]

    return l1[0] < e2[0] and l1[1] < e2[1] and l2[0] < e1[0] and l2[1] < e1[1]

print(rectangleOverlap(rec1_1, rec2_1))     # True
print(rectangleOverlap(rec1_2, rec2_2))     # False
print(rectangleOverlap(rec1_3, rec2_3))     # False