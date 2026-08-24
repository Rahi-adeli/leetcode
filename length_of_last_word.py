s= "luffy is still joyboy"

def lengthOfLastWord(s):
    words = s.split()
    length = len(words[-1])
    return length


result = lengthOfLastWord(s)
print(result)