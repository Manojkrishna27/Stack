def previous_smaller(arr):
    res=[]
    stack=[]
    for x in arr:
        while stack and stack[-1]>=x:
            stack.pop()
        if not stack:
            res.append(-1)
        else:
            res.append(stack[-1])
        stack.append(x)
    return res
arr=list(map(int,input().split()))
print(previous_smaller(arr))