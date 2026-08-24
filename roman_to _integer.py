 
s= input("roman number:")
values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

def  roman_to_integer(values,s):
    
    total = 0
    
    for i in range (0 , (len(s))):
        current_value = values [s[i]]
        
        if  i+1 < len(s):
         next_value = values [s[i+1]]

         if current_value >= next_value :
               total += current_value

         elif current_value < next_value:
         
               total -= current_value
        else:
            total += current_value     
         

    return total


result= roman_to_integer(values , s)
print (result)