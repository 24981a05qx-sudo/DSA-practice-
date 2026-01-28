#Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. Determine the maximum profit achievable by buying and selling the stock at most once. 

#The stock should be purchased before selling it, and both actions cannot occur on the same day.


#Example 1

#Input: arr = [10, 7, 5, 8, 11, 9]
#Output: 6
#Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.

#Example 2:

#Input: arr = [5, 4, 3, 2, 1]
#Output: 0
#Explanation: In this case, no transactions are made. Therefore, the maximum profit remains 0.


arr = list(map(int, input("Enter the array elements: ").split()))
n = len(arr)

min_price = float('inf')  
max_profit = 0             

for price in arr:
   
    if price < min_price:
        min_price = price

    profit = price - min_price
    
    
    if profit > max_profit:
        max_profit = profit

if max_profit > 0:
    print("Profit:", max_profit)
else:
    print("0 No Loss No Profit")

