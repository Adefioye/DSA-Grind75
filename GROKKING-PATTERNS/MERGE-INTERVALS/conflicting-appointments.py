appointments1 =  [[1,4], [2,5], [7,9]]
#false
appointments2 = [[6,7], [2,4], [8,12]]
# true
appointments3 = [[4,5], [2,3], [3,6]]
#false

def conflictingAppointments(appointments):
    l = 0
    r = l + 1

    appointments.sort(key=lambda item: item[0])

    while r < len(appointments):
        s1, e1 = appointments[l]
        s2, e2 = appointments[r]

        if e1 >= s2  and e2 >= s1:
            return False
        
        l += 1
        r = l + 1
    
    return True

print(conflictingAppointments(appointments1))
print(conflictingAppointments(appointments2))
print(conflictingAppointments(appointments3))