#You are given an integer n. Return the value of n! or n factorial.



#Factorial of a number is the product of all positive integers less than or equal to that number.


#Example 1

#Input: n = 2

#Output: 2

#Explanation: 2! = 1 * 2 = 2.

#Example 2

#Input: n = 0

#Output: 1

#Explanation: 0! is defined as 1.

def fact(n):
    if n<0:
        
        return "Fctorial of number is inappropriate"
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    

n=int(input("Enter the number:"))

value=fact(n)
print("Factorial of given number is :", value)