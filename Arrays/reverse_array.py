size=int (input("Enter the size of the array: "))

arr=[]
for i in range(size):
    element=int(input("Enter element:"))
    arr.append(element)

print("Original Array:",arr)

print("Revesed Array:",arr[::-1])
