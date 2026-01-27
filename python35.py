#Given an array of integers nums and an integer target.
#  Return the indices(0 - indexed) of two elements in nums such that they add up to target.

#Each input will have exactly one solution, and the same element cannot be used twice.

#Example 1

#Input: nums = [1, 6, 2, 10, 3], target = 7
#Output: [0, 1]
#Explanation:
#nums[0] + nums[1] = 1 + 6 = 7

#Example 2

#Input: nums = [1, 3, 5, -7, 6, -3], target = 0
#Output: [1, 5]
#Explanation:

nums[1] + nums[5] = 3 + (-3) = 0



arr=list(map(int,input("Enter the elements of the array:").split()))
n=len(arr)
target=int(input("Enter ur desired target:"))

value=[]

for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==target:
            value=[i,j]
            break
        if value:
            break

print("The indices of two elements who's sum is equivalent to target is :",value)