result='';
for i in range(100):
    result ='';
    if i%3 == 0:
        result = 'Fizz'
    if i%5 == 0:
        result += 'Buzz'
    if(result):
        print(result)