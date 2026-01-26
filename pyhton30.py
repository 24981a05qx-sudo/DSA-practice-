arr1=list(map(int,input("Enter the elements of the first array:").split()))
arr2=list(map(int,input("Enter the elements of th esecond array:").split()))
n1=len(arr1)
n2=len(arr2)
new=[]
for i  in arr1:
    if i not in new:
        new.append(i)


for i in arr2:
    if i not in new:
        new.append(i)

print("Uninon of two arrays is:",new)

