from distutils.log import error


def countPairs2(arr, sum):
    map={};
    for i in arr:
        if i in map:
            map[i] +=1
        else:
            map[i]=1

    count = 0;
    for j in arr:
        try:
            count += map[sum-j]
            if sum-j == j:
                count = count -1
        except Exception:
            pass


    return count//2
print(countPairs2([1,2,2,4,5,3],5))