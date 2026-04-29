class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedliststack:
    def __init__(self):
        self.head=None

    def push(self,x):
        new_node=Node(x)
        new_node.next=self.head
        self.head=new_node

    def pop(self):
        if self.head==None:
            print("stack underflow")
            return-1
        val=self.head.data
        self.head=self.head.next
        return val
    def top_element(self):
        if self.head is None:
            return-1
        return self.head.data
    
    def isempty(self):
        return self.head is None
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
s=linkedliststack()
s.push(10)
s.push(20)
s.push(30)
print(s.display())
print(s.top_element())
print(s.pop())
s.display()
