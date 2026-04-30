def nextsmaller(arr):
    stack=[]
    res=[]

    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]>=arr[i]: # fir next smaller we want to compare stack[-1](top)>=arr[i]
            stack.pop()

        if stack:
            res.append(stack[-1]) # we can also append this 
        stack.append(arr[i])
    return res[::-1]  # but make sure we want to reverse
arr=list(map(int,input().split()))
print(nextsmaller(arr))