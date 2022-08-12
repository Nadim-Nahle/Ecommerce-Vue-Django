from operator import truediv


def isAnagram(array1,array2):
    if len(array1) != len(array2):
        return False
    else:
        array1.sort();
        array2.sort();
        if(array1 == array2):   
            return True
        else:
            return False

array1 = [1,2]
array2 = [1,2,2]

print(isAnagram(array1,array2))