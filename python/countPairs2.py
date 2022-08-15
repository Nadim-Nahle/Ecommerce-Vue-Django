def countPairs2(arr, sum):
    map={};
    for i in arr:
        if i in map:
            map[i] +=1
        else:
            map[i]=1
    print(map)
    count = 0;
    for j in arr:
        count += map[sum-j]
        if sum-j == j:
            count = count -1

    print(count//2)
countPairs2([1,2,2,1],3)