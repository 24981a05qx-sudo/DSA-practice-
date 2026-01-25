#Given an array of integers nums, return the value of the largest element in the array


#Example 1

#Input: nums = [3, 3, 6, 1]
#Output: 6
#Explanation: The largest element in array is 6

#Example 2

#Input: nums = [3, 3, 0, 99, -40]
#Output: 99
#Explanation: The largest element in array is 99




arr=list(map(int,input("Enter the elements of the array:").split()))
n=len(arr)
max=arr[0]
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

print("The largest element in the array is:",max)