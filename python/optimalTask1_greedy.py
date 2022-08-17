def optimalTask1(arr):
    arr = sorted(arr)
    for i in range(len(arr)//2):
            print(arr[i],arr[~i])
    

optimalTask1([6,3,2,7,5,5])