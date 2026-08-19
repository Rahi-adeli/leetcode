nums= [1,3,7,4,9]
target= 11
length=len(nums)

def two_sum (nums , target):

    for index1 in range(length):
        for index2 in range(index1 + 1, length):
            sum = nums[index1] + nums[index2] 
            if sum == target:
              return [index1,index2]
        
result= two_sum(nums,target)
print (result)