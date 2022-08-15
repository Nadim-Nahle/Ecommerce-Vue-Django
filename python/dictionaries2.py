phoneBook = {
    'jane': 'jane@gmail.com'
}

def search(dic):
    x = input('to search for a name press s\nto delete a name press d\nto add a name press a\nto edit a name press e ')
    if x == 's':
        name = input('please enter a name to see their email\n')
        return dic[name]
    if x == 'd':
        delete = input('please enter a name to delete\n')
        dic.pop(delete)
        return dic
    if x == 'e':
        edit = input('please enter a name to edit\n')
        newEmail = input('please enter the new email\n')
        dic[edit] = newEmail
        return dic

print(search(phoneBook))