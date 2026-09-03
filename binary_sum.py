a = "1010"
b = "1011101"

def addBinary(a, b):

   
    max_length = max(len(a), len(b))
    a = a.zfill (max_length)
    b = b.zfill (max_length)

    i = len(a)-1
    j = len(b)-1
    carry = 0
    result = ""

    while i >= 0 or j >= 0:
        sum = int (a[i] + b[j]) 
        if sum == 0:
            result +="0"
            carry = 0
        elif sum == 1:
            result +="1"
            carry = 0
        elif sum  == 2:
            result +="0"
            carry = 1
        elif sum == 3:
            result += "1"
            carry = 1

