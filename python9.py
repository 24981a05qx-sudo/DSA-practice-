#You are given two integers n1 and n2.
#  You need find the Greatest Common Divisor (GCD) of the two given numbers. Return the GCD of the two numbers.



#The Greatest Common Divisor (GCD) of two integers is the largest positive integer that divides both of the integers.


#Example 1

#Input: n1 = 4, n2 = 6
#Output: 2
#Explanation: Divisors of n1 = 1, 2, 4, Divisors of n2 = 1, 2, 3, 6
#Greatest Common divisor = 2.



#Example 2

#Input: n1 = 9, n2 = 8
#Output: 1
#Explanation: Divisors of n1 = 1, 3, 9 Divisors of n2 = 1, 2, 4, 8.
#Greatest Common divisor = 1.

n1 = int(input())
n2 = int(input())

div1 = []
div2 = []

for i in range(1, n1+1):
    if n1 % i == 0:
        div1.append(i)

for i in range(1, n2+1):
    if n2 % i == 0:
        div2.append(i)

common = list(set(div1) & set(div2))
common.sort()

print(common[-1])