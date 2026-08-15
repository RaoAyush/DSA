n=int(input("Enter the  total number of floors: "))
arr=[]
for i in range(n):
    x=int(input("Enter the number of floor "))
    arr.append(x)

time=arr[0]
for i in range(0,n-1):
    time +=abs(arr[i]-arr[i+1])

print("Total time taken to reach last floor is ", time)