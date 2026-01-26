#Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.


#Example 1

#Input : nums = [1, 2, 2, 4, 3, 1, 4]
#Output : 3
#Explanation : The integer 3 has appeared only once.

#Example 2

#Input : nums = [5]
#Output : 5
#Explanation : The integer 5 has appeared only once.



arr=list(map(int,input("Enter the array elements:").split()))
n=len(arr)
for i in range(n):
    count=0
    for j in range(n):
        if arr[i]==arr[j]:
            count+=1

    if count==1:
         print("The number that appeared once is:",arr[i])
         break