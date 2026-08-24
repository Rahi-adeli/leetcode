
digits = list(map(int, input("enter your array:").split()))


def plus_one (digits):
    length = len(digits)
    carry = True
    
    for i in range (length-1, -1, -1):
            if  digits [i] == 9:
                digits [i] = 0

            elif digits[i]  < 9 :
                 digits[i]+=1
                 carry = False

                 break 
            
                 

    if carry == True:
          digits.insert(0,1)  



'''

                        class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        carry = True

        for i in range(length-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            elif digits[i] < 9:
                digits[i] += 1
                carry = False
                break

        if carry == True:
            digits.insert(0, 1)'''