num = 38

def addDigits(num):

    while num > 9:
        total = 0
        num_str = list(str(num))
        for i in range ( len (num_str)):
            total += int(num_str[i])
        num = total
    return num

    


result = addDigits (num)
print(result)