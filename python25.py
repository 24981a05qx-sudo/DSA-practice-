#Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.


#Example 1

#Input : nums = [1, 2, 3, 4, 5]
#Output : true
#Explanation : For all i (1 <= i <= 4) it holds nums[i] <= nums[i+1], hence it is sorted and we return true.

#Example 2

#Input : nums = [1, 2, 1, 4, 5]
#Output : false
#Explanation : For i == 2 it does not hold nums[i] <= nums[i+1], hence it is not sorted and we return false.

arr=list(map(int,input("Enter the array elements:").split()))
n=len(arr)
flag=0


for i in range(0,n-1):
    if arr[i]<arr[i+1]:
        flag+=1
        
if flag==n-1:
    print("Array is  sorted")
else:
    print("Array is not sorted")