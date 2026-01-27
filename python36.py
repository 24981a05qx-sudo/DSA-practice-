#Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.



#The sorting must be done in-place, without making a copy of the original array.


#Example 1

#Input: nums = [1, 0, 2, 1, 0]
#Output: [0, 0, 1, 1, 2]
#Explanation:
#The nums array in sorted order has 2 zeroes, 2 ones and 1 two

#Example 2:

#Input: nums = [0, 0, 1, 1, 1]
#Output: [0, 0, 1, 1, 1]
#Explanation:
#The nums array in sorted order has 2 zeroes, 3 ones and zero twos


nums =list(map(int,input("Enter the elements of the array:").split()))

count0 = 0
count1 = 0
count2 = 0


for num in nums:
    if num == 0:
        count0 += 1
    elif num == 1:
        count1 += 1
    else:
        count2 += 1

index = 0
for _ in range(count0):
    nums[index] = 0
    index += 1
for _ in range(count1):
    nums[index] = 1
    index += 1
for _ in range(count2):
    nums[index] = 2
    index += 1

print(nums) 