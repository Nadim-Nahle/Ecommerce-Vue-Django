from collections import Counter;

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        return Counter(s1) == Counter(s2)


s1=[1,2,1]
s2=[1,2,3]

print(isAnagram(s1,s2))