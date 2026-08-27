nums = [9,6,4,2,3,5,7,0,10,8,11]

def missingNumber(nums):
    length = len (nums)
    n = length * (length + 1) 
    sum = n / 2 
    total = 0
    for i in range (length):
        total += nums[i]


    number = sum - total

    return number

result = missingNumber(nums)
print (result)

    
