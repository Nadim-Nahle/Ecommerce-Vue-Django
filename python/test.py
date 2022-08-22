def largestSum(arr):
    l=0
    r=1
    maxs = 0
    for l in range(len(arr)-1):
        for r in range(len(arr)):
            maxs = max(arr[l]+[arr[r]])
        