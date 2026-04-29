class Arraystack:
    def __init__(self,size):
        self.stack=[0]*size
        self.top=-1

        self.size=size
    def push(self,x):
        if self.top==self.size-1:
            print("stack overflow")
            return
        self.top+=1
        self.stack[self.top]=x

    def pop(self):
        if self.top==-1:
            print("Stack underflow")
            return -1
        val=self.stack[self.top]
        self.top=-1
        return val
    def topelement(self):
        if self.top==-1:
            return-1
        return self.stack[self.top]
    def isempty(self):
        return self.top==-1
s=Arraystack(5)
s.push(5)
s.push(10)
s.push(15)
s.push(20)
s.push(25)
print(s.topelement())
print(s.pop())
print(s.topelement())
print(s.isempty())