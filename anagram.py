s = "anagram"
t = "nagaram"


def isAnagram(s, t):
    
    if sorted(t) == sorted(s):
        return True
    else:
        return False


result = isAnagram(s,t)
print(result)
    