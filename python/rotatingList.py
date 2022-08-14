#LINEAR SEARCH
def rotated(arr):
    arr1 = arr.copy()
    arr.sort();
    t = arr[0];
    for i in range(len(arr1)):
        if arr1[i] == t:
            return i

arr=[5,6,9,0,2,3,4]
arr1=[5,6,9,0,2,3,4]

print(rotated(arr))


