prices = [7,1,5,3,6,4,10,0,2]

def maxProfit(prices):
    length = len (prices)
    minimum = prices[0]
    difference = 0
    profit = 0
    for i in range (length):
        if minimum > prices [i]:
            minimum = prices[i]

        if minimum < prices [i]:
            difference = prices[i] - minimum
            
       
            if  profit < difference :
                profit = difference
    return profit


result = maxProfit(prices)
print (result)