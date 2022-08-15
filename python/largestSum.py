from operator import truediv


def largestSum(arr, x):
    dic = {};
    for i in range(len(arr)):
        dic[i] = arr[i]
    
    for j in arr:
        try:
            if dic[j] + arr[j+1] == x:
                return True
        except:
            False
    return False



print(largestSum([1,2,4],6))