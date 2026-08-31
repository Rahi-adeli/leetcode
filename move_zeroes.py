nums = [ 0, 1, 2, 0, 3, 0, 0, 4, 6, 0]

def moveZeroes(nums):
    
    begining = 0
    ending = len(nums) -1 
    while begining < ending:
        if nums[begining] == 0: 
            if nums[ending]!=0:
                nums[begining],nums[ending] = nums[ending],nums[begining]

                ending-=1
                begining

        
    return nums


result = moveZeroes(nums)
print (result)