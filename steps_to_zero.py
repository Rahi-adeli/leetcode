num = 123

def numberOfSteps(num):
    count = 0
    while num != 0:
        if num % 2 == 0:
            num = num //2
            count +=1
        else:
            num = num - 1
            count +=1
    return count


result = numberOfSteps(num)
print(result)