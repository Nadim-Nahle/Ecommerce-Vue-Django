def maxarray(array,n):
    maximum = array[0]
    res = array[0];
    for i in range(1,n):
        maximum = max(maximum + array[i], array[i])
        res = max(res,maximum)
    print(res)

array=[1,-2,5,-9,-3-3-3,6]  
n = len(array);

maxarray(array,n)

