def stock_span(arr):
    n=len(arr)
    res=[0]*n
    stack=[] # pattern monotonic decrease stack
    for i in range(n):
        while stack and arr[stack[-1]]<=arr[i]: # this problem is same as previous greater element on left but storing its index 
            stack.pop()

        if not stack:
            res[i]=i+1
        else:
            res[i]=i-stack[-1]
        stack.append(i)
    return res
arr=[100,80,60,70,60,75,85]
print(stock_span(arr))