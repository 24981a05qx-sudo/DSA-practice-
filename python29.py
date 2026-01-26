#Given an integer array nums, move all the 0's to the end of the array.
#  The relative order of the other elements must remain the same.



#This must be done in place, without making a copy of the array.


#Example 1

#Input: nums = [0, 1, 4, 0, 5, 2]

#Output: [1, 4, 5, 2, 0, 0]

#Explanation:

#Both the zeroes are moved to the end and the order of the other elements stay the same

#Example 2

#Input: nums = [0, 0, 0, 1, 3, -2]

#Output: [1, 3, -2, 0, 0, 0]

#Explanation:

#All 3 zeroes are moved to the end and the order of the other elements stay the same





arr=list(map(int,input("Enter the elements of the array:").split()))
n=len(arr)
flag=0

for i in range(0,n-1):
    if arr[i]==0:
        flag=flag+n-1
        
        
for j in range(0,flag):
    
    for i in range(0,n-1):
        if arr[i]==0:
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp


print("Array after moving 0's to end:",arr)
