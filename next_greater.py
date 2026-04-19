def next_greater(arr):
    n=len(arr)
    res=[-1]*n
    stack=[]
    

    for i in range(n-1,-1,-1):
        
        # this loop will remove smaller elements
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        # if stack not empty it stores large elements
        if stack:
            res[i]=stack[-1]
        # push current element for checking
        stack.append(arr[i])
    return res
print(next_greater([2,3,1,5,25]))