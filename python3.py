# Problem: Print numbers from 1 to N
# Constraints: N is a positive integer
# The program prints all numbers from 1 up to N using a while loop

# Take input from user
n=int(input("Enter a positive number n: "))

i = 1
sum=0
while i <= n:
    sum=sum+i
    i=i+1
print(sum) 
