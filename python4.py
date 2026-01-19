# Problem: Calculate square of a number using a function
# Constraints: Input is a positive integer

# Define a function to calculate square fo a given number 
def square(num):
    return num * num


num = int(input("Enter a number: "))


result = square(num)
print(f"The square of {num} is {result}")