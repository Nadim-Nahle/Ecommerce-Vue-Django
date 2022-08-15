def simplified(str):
    stack = [];
    arr = str.split('/')
    for i in range(len(arr)):
        if arr[i] == '..' and stack:
            stack.pop()
        else:
            stack.append(arr[i])
    return '/'.join(stack)

print(simplified('b/../c/d/../a/g'))