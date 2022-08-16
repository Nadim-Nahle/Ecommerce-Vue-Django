def smallest(arr):
    small = 1;
    arr.sort()
    for i in arr:
        if i==small:
            small+=1
    return small

    
print(smallest([1,2,3,4,-1,6,5]))