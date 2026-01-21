#You are given an integer n. 
# You need to check whether the number is a palindrome number or not. 
# Return true if it's a palindrome number, otherwise return false.



#A palindrome number is a number which reads the same both left to right and right to left.


#Example 1
#Input: n = 121
#Output: true

#Explanation: When read from left to right : 121.
#When read from right to left : 121.

#Example 2
#Input: n = 123
#Output: false
#Explanation: When read from left to right : 123.
#When read from right to left : 321.

n=int(input("Enter the number:"))
pal=0
c=0
num=n
while n>0:

    c=n%10
    n=n//10
    pal=pal*10+c

if pal==num:
    print("True")
else :
    print("False")
