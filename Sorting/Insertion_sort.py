num=int(input("the number of elements: "))
arr=[]
for i in range(num):
    element=int(input("Enter the element: "))
    arr.append(element)

for i in range(1,num):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key

print("The sorted array is: ",arr)