number=int (input("gimme some numbers:"))



def fizzBuzz(number):
  answer=[]
  for num in range (1 ,number+1):

    if num % 3 == 0 and num % 5 == 0 :
      answer.append ("FizzBuzz")
    elif num % 3 == 0:
      answer.append("Fizz")
    elif num % 5 == 0:
      answer.append ("BUZZ")

    else:
      answer.append (str(num))

  return answer


result= fizzBuzz(number)
print (result)




'''
class Solution(object):
    def fizzBuzz(self, n):
       
        answer=[]
        for num in range (1 ,n+1):

            if num % 3 == 0 and num % 5 == 0:
                answer.append ("FizzBuzz")
            elif num % 3 == 0:
                answer.append("Fizz")
            elif num % 5 == 0:
                answer.append ("Buzz")
            else:
                 answer.append (str(num))

        return answer
        
'''
