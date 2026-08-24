nums = [1, 2, 1, 3, 1, 1, 3, 3, 4, 6, 2, 4]

def numIdenticalPairs(nums):

    count = 0
    length = len(nums)
    for index_1 in range (length):
        for index_2 in range (index_1 +1 , length):
            if nums[index_1] == nums[index_2]:
                count+=1               

    return count


result = numIdenticalPairs(nums)
print (result)