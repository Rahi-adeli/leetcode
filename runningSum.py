nums=[1,2,3,4,5,6]

def runningSum(nums):

    total = 0
    keeper = []
    length = len (nums)

    for i in range (length):
        total += nums[i]
        keeper.append(total)

    return keeper


result = runningSum(nums)
print (result)