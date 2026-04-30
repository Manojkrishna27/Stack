def daily_temperature(arr):
    n=len(arr)
    res=[0]*n
    stack=[]

    for i in range(n):
        while stack and arr[i]>arr[stack[-1]]: # comparing the index value

            previous=stack.pop()
            res[previous]=i-previous    # subtracting the index value of boh prev and now we get daily temperatue
        stack.append(i)   # storeing the index 

    return res
arr=[73,74,75,71,69,72,76,73]
print(daily_temperature(arr))