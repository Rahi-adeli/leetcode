import math

n = 16

def isPowerOfTwo(n):

    if n <= 0:
        value = False
    else:
        power_of_tow = round(math.log(n,2))
        value_check = 2 ** power_of_tow

   
        if value_check == n :
            value = True 
        else:
            value = False

    return value


result = isPowerOfTwo(n)
print(result)



    