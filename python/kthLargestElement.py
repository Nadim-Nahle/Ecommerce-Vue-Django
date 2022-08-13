def findLargest(arr,k):
    arr.sort()
    return arr[k-1];


arr=[1,6,3,4]
k=3

print(findLargest(arr,k))