#Given a binary array nums, return the maximum number of consecutive 1s in the array.

#A binary array is an array that contains only 0s and 1s.


#Example 1

#Input: nums = [1, 1, 0, 0, 1, 1, 1, 0]
#Output: 3

#Explanation:
#The maximum consecutive 1s are present from index 4 to index 6, amounting to 3 1s

#Example 2:

#Input: nums = [0, 0, 0, 0, 0, 0, 0, 0]
#Output: 0

#Explanation:
#No 1s are present in nums, thus we return 0
#nums = list(map(int, input("Enter binary array elements separated by space: ").split()))

count= 0
temp = 0

for i in nums:
    if i == 1:
        temp+= 1
        if temp>count:
            count=temp
    else:
        temp= 0

print("Maximum consecutive 1s:",count)