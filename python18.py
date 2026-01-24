#Given a string s, return true if the string is palindrome, otherwise false.

#A string is called palindrome if it reads the same forward and backward.


#Example 1

#Input : s = "hannah"
#Output : true
#Explanation : The string when reversed is --> "hannah", which is same as original string , so we return true.

#Example 2

#Input : s = "aabbaA"
#Output : false
#Explanation : The string when reversed is --> "Aabbaa", which is not same as original string, So we return false.

def check_palindrome(s):
    if s== "":
        return s
    return check_palindrome(s[1:])+s[0]

s=input("Enter your string:")


if s== check_palindrome:
    print("True")
else :
    print("False")