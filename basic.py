stack=[]

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# pop removes the top element
stack.pop()
print(stack)

# view top/peek element
print(stack[-1])

# isempty()
print(len(stack)==0) # False
