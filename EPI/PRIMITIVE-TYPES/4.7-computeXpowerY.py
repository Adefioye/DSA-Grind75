def power(x, y):

    res, power = 1, y 

    if y < 0:
        power, x = -power, 1/x 

    while power:

        if power & 1:
            res *= x
        
        x, power = x * x, power >> 1 

    return res 



