import itertools;

def validParenth(str):
    arr=[];
    closeToOpen = {
        '}':'{',
        ')':'(',
        '}':'{'
    }

    for i in str :
        if i in closeToOpen:
            if arr and arr[-1] == closeToOpen[i]:
                arr.pop()
            else:
                return False
        else:
            arr.append(i)
    return True if not arr else False


arr1=['(','(',')']
