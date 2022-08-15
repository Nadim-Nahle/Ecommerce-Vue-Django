import queue
def isPalindrome(str):
    stack1=[];
    stack2=[];
    temp=[];
    for i in range(len(str)):
        stack1.append(str[i])
    temp = stack1.copy()
    for i in stack1:
        stack2.append(temp.pop())
    
    if(stack1 == stack2):
        return True
    else:
        return False

print(isPalindrome('omheleho'))