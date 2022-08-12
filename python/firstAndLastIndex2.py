from re import T

def findStart(arr,t,left,right):
    if arr[0] == t:
        return 0;
    if (right > left):
        mid = (right+left) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t :
            return findStart(arr,t,left,mid-1)
        else:
            return findStart(arr,t,mid+1,right)
    else:
        return -1

def isTarget(arr, t):
    if len(arr) == 0:
        return[-1,-1]
    start = findStart(arr,t,left,right)
    if start == -1:
        return[-1,-1]
    end = start;
    while end + 1 < len(arr) and arr[end+1] == t:
        end = end +1
    return[start,end]

arr=[1,2,3,4,4,5]
t = 4
left=arr[0]
right=arr[-1]

print(isTarget(arr,t))
    