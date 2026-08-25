jewels = "aAc"
stones = "aAAacCabbbb"

def numJewelsInStones(jewels, stones):
    j_char= list(jewels)
    s_char= list(stones)
    count = 0

    for char in s_char:
        if char in j_char:
            count+=1
    return count

result = numJewelsInStones(jewels, stones)
print (result)