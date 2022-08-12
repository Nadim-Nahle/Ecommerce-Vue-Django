def isTarget(arr,t):
    for i in range(len(arr)):
        if arr[i]==t:
            start = i
            while i+1 < len(arr) and arr[i+1] == t:
                i += 1
            return [start,i]
    return[-1,-1]

arr = [1,1,1,1,1,2,2,4]
t = 1
print(isTarget(arr,t))
