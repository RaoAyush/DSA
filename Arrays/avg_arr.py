n=int(input("Enter the size of the array:  "))
arr=[]
for i in range(n):
    x=int(input("Enter the elements of array: "))
    arr.append(x)
print("The original array is: ",arr)

if n<3:
    print("The array should have at least 3 elements to remove the maximum and minimum elements and calculate the average: ")
else:
    sum=0
    maxm=max(arr)
    minm=min(arr)
    count=0

    for i in range(n):
        if arr[i]!=maxm and arr[i]!=minm:
            sum+=arr[i]
            count+=1
    
    if count==0:
        print("No element is remaining to calculate the average after removing the maximim and minimum elements: ")
    else:
        avg=sum/count
        print("the average of the array after removing the maximum and minimum elements is: ",avg)

