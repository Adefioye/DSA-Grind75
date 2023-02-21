appointments1 =  [[1,4], [2,5], [7,9]]
#false
appointments2 = [[6,7], [2,4], [8,12]]
# true
appointments3 = [[4,5], [2,3], [3,6]]
#false

def conflictingAppointments(appointments):

    appointments.sort(key=lambda x: x[0])

    l = 0

    for r in range(1, len(appointments)):
        s1, e1 = appointments[l]
        s2, e2 = appointments[r]

        if s2 < e1:
            return False

        l += 1

    return True

print(conflictingAppointments(appointments1))
print(conflictingAppointments(appointments2))
print(conflictingAppointments(appointments3))

# def conflictingAppointments(appointments):

#     appointments.sort(key=lambda x: x[0])

#     output = [appointments[0]]

#     for start, end in appointments[1:]:
#         prevEnd = output[-1][1]

#         if start < prevEnd:
#             return False
        
#         output.append([start, end])
    
#     return True


# def conflictingAppointments(appointments):
#     l = 0
#     r = l + 1

#     appointments.sort(key=lambda item: item[0])

#     while r < len(appointments):
#         s1, e1 = appointments[l]
#         s2, e2 = appointments[r]

#         if e1 >= s2  and e2 >= s1:
#             return False
        
#         l += 1
#         r = l + 1
    
#     return True
