#Given an array of integers nums, return the second-largest element in the array. 
# If the second-largest element does not exist, return -1.


#Example 1

#Input: nums = [8, 8, 7, 6, 5]
#Output: 7
#Explanation:
#The largest value in nums is 8, the second largest is 7

#Example 2

#Input: nums = [10, 10, 10, 10, 10]
#Output: -1
#Explanation:
#The only value in nums is 10, so there is no second largest value, thus -1 is returned


arr=list(map(int,input("Enter the array elements:").split()))
n=len(arr)

largest=arr[0]
second=0

for i in range(1,n):
    if arr[i]>largest:
        second=largest
        largest=arr[i]
    elif arr[i]>second:
        second=arr[i]

print("The second largest element in the array is:",second)


