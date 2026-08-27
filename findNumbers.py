nums = [555,901,482,1771]

def findNumbers(nums):
    numbers = []
    for i in range (len(nums)):
        num = str (nums [i])
        length = len(num)

        if length % 2 == 0:
            numbers.append(num)
            
    return len(numbers)



result = findNumbers(nums)
print (result)