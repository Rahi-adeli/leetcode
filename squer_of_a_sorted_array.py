nums = [-7,-3,2,3,11,16]

def sortedSquares(nums):
    numbers = []
    for i in range (len(nums)):
        new_num = nums[i] ** 2
        numbers.append(new_num)
        sorted_numbers = sorted(numbers)

    return sorted_numbers


result = sortedSquares(nums)
print (result)