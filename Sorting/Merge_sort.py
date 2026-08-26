class Solution:
    def merge_sort(self,arr,l,r):
        if l>=r:
            return
        mid=(l+r)//2
        self.merge_sort(arr,l,mid)
        self.merge_sort(arr,mid+1,r)

        self.merge(arr,mid,l,r)

    def merge(self,arr,mid,l,r):
        n=[]
        m=[]
        for i in range(l,mid+1):
            n.append(arr[i])
        for j in range(mid+1,r+1):
            m.append(arr[j])

        i,j,k=0,0,l

        while i<len(n) and j<len(m):
            if n[i]<m[j]:
                arr[k]=n[i]
                i+=1
            else:
                arr[k]=m[j]
                j+=1
            k+=1
        while i<len(n):
            arr[k]=n[i]
            i+=1
            k+=1
        while j<len(m):
            arr[k]=m[j]
            j+=1
            k+=1
        
arr = list(map(int,input("Enter the elements of array :").split()))
obj=Solution()
obj.merge_sort(arr,0,len(arr)-1)
print("After sorting the array is : ",arr)