nums = [2,2,1,1,1,2,2,2,2,2,2]

def majorityElement(nums):
    length = len(nums)
    nums = sorted (nums)
    count = 0
    n = length / 2
    seen = {}
    
    
    for i in range (length-1):
       current_num = nums[i]
       next_num = nums [i+1]

       if current_num == next_num:
           count +=1

       else:
           seen [nums[i]] = nums[i+1]
           seen [nums[i]] = count + 1
           count = 0   

    
    seen[nums[-1]] = count + 1
    majority = max (seen, key=seen.get)
    return majority
       


result = majorityElement(nums)
print (result)