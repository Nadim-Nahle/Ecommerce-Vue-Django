import matplotlib.pyplot as plt
import math;


def sum(arr, n):
    res = arr[0];
    for i in range(n):
        curr = 0;
        for j in range(n):
            curr = curr + arr[j]
            res = max(res, curr)
            
        return res;

arr = [1,2,-4,5,-3,-2,4,-2,-1,-4,6,-3]
n= len(arr)

print(sum(arr,n))


                    