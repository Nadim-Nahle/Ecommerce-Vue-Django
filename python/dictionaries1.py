import random

states = {
    'new york' : 'albany',
    'california' : 'sacramento',
    'florida' : 'tallahasi',
    'texas' : 'austin',
    'washinton' : 'olympia',
    'colorado' : 'denver'
}
  
def isCapital(dic):
    sum = 0;
    i = 0;
    while(i<3):
        x = random.choice(list(dic.keys()))
        y = input('please enter a the capital of %s ' % x)
        if states[x] == y :
            sum+=1;
        dic.pop(x)
        i += 1;
    print(sum)

isCapital(states)
