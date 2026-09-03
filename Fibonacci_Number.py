n = 8
def fib(n):
    a = 0
    b = 1
    
    
    while count < n:
        fibo = a + b
        a = b 
        b = fibo
            
        count +=1

    return a


result = fib(n)
print (result)