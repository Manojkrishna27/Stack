def daily_temperature(arr):
    n=len(arr)
    res=[0]*n
    stack=[]

    for i in range(n):
        while stack and arr[i]>arr[stack[-1]]:
            previous=stack.pop()
            res[previous]=i-previous
        stack.append(i)

    return res
arr=[73,74,75,71,69,72,76,73]
print(daily_temperature(arr))