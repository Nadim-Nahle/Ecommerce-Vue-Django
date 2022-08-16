def mostCon(arr):
    sum = 0;
    maximum = 0;
    for i in arr:
        if i == 0:
            sum +=1
        else:
            maximum = max(sum,maximum)
            sum = 0
    return max(maximum,sum)

print(mostCon([0,0,0,1,3,0,0,0,0]))

    


