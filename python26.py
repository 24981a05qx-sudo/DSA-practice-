#







arr=list(map(int,input("Enter the elements of the array in order:").split()))

unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)

print("Array after removing duplicates is: ",unique)