def isDigit(number):
    sum = 0;
    newNumber = str(number)
    for i in (newNumber):
        sum = sum + int(i)
    print(sum)
    if sum <= 10 :
        return sum
    else:
        isDigit(sum)


print(isDigit(128))