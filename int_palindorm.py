x = 121

def isPalindrome(x):
    new_x = list (str (x))
    x_prim = list(reversed (new_x)) 

    if new_x == x_prim:
        return True
    else:
        return False


result = isPalindrome(x)
print (result)