#You are given an integer n. You need to check if the number is prime or not. 
# Return true if it is a prime number, otherwise return false.



#A prime number is a number which has no divisors except 1 and itself.


#Example 1

#Input: n = 5
#Output: true
#Explanation: The only divisors of 5 are 1 and 5 , So the number 5 is prime.

#Example 

#Input: n = 8
#Output: false
#Explanation: The divisors of 8 are 1, 2, 4, 8, thus it is not a prime number

num=int(input("Enter the number:"))
flag=0
for i in range(1,num//2):
    if num%i==0:
        flag+=1


if flag>1:
    print("The given number is not a prime number")
else :
    print("The given number is a prime number")