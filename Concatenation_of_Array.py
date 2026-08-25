nums = [1,3,2,1,4,6,7]

def getConcatenation(nums):
    concat = nums + nums

    return concat


''' or just simply
 
 def getConcatenation(self, nums):
        
        return nums * 2'''

result = getConcatenation(nums)
print (result)