nums = [4,1,2,1,2]

def singleNumber(nums):
    seen = {}

    for n in nums:
        if n in seen:
            del seen[n]
        else:
                seen[n] = n
    return list(seen.keys())


result = singleNumber(nums)
print (result)