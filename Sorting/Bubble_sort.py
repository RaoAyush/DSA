num=int(input("the number of elements: "))
list_1=[]
for i in range(num):
    element=int(input("Enter the element: "))
    list_1.append(element)

for i in range(num):
    for j in range(0,num-i-1):
        if list_1[j]>list_1[j+1]:
            list_1[j],list_1[j+1]=list_1[j+1],list_1[j]
print("the sorted array is : ", list_1)