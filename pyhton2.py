#Given the integer day denoting the day number, 
# print on the screen which day of the week it is. 
# Week starts from Monday and for values greater than 7 or less than 1, print Invalid.
#Ensure only the 1st letter of the answer is capitalised.



#Example 1

#Input: day = 3
#Output: Wednesday

#Example 2

#Input: day = 8
#Output: Invalid

num = int(input("Enter the day number: "))

switch = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

print(switch.get(num, "Invalid input"))