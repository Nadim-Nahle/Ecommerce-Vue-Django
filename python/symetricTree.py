def areSymetric(root1,root2):
    if root1 is None and root2 is None:
        return True
    elif root1 != root2:
        return False
    else:
        areSymetric(root1.left, root2.right) and areSymetric(root1.right, root2.left)

def isSysmetric(root):
    if root is None:
        return False
    else:
        return areSymetric(root.left, root.right)