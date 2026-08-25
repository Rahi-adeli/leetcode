nums = [1,2,3,4,5,5,4,3,2,1]
n = 5

def shuffle(nums, n):
    numbers = []
    for i in range (n):
            numbers.append(nums[i])
            numbers.append(nums[i+n])

    return numbers


result = shuffle(nums, n)
print(result)