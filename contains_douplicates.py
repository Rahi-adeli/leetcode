'''nums = [1,1,1,3,3,4,3,2,4,2]

def containsDuplicate(nums):
    length = len(nums)
    doup = False
   
    for index_1 in range (length):
        for index_2 in range (index_1 + 1 , length):
           if nums[index_1] == nums [index_2]:
               doup = True
               seen.append
           

    return doup


result = containsDuplicate (nums)
print (result)






**
runtime error
**

'''


nums = [1,1,1,3,3,4,3,2,4,2]

def containsDuplicate(nums):
    length = len(nums)
    nums.sort()
    doup = False
    
    for i in range (length-1):
        if nums[i] == nums [i+1]:
            doup = True

    return doup
    
    
result = containsDuplicate (nums)
print (result)


#got accepted but it was very slow