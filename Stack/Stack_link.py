class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.size=0
        self.top=None
    def push(self, x):
        newNode=Node(x)
        if self.top==None:
            self.top=newNode
        else:
            newNode.next=self.top
            self.top=newNode
        self.size+=1
    def pop(self):
        if self.top==None:
            return None
        else:
            x=self.top.data
            self.top=self.top.next
            self.size-=1
            return x
    def getTop(self):
        if self.top==None:
            return None
        else:
            return self.top.data

    def isEmpty(self):
        if self.top==None:
            return True
        else:
            return False
    def getsize(self):
        return self.size



st=Stack()
st.push(10)
st.push(22)
st.push(30)
print(st.getsize())
print(st.getTop())
print(st.pop())
print(st.isEmpty())



