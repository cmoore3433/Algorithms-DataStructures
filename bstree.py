class Node: 
    def __init__(self, key, data): 
        self.left=None
        self.right=None
        self.parent=None
        self.key=key 
        self.data=data
        
class BST:
    def __init__(self):
        self.root=None
    
def treeInsert(tree, node):
    y=None
    x=tree.root
    while x is not None:
        y=x
        if node.key < x.key:
            x=x.left
        else:
            x=x.right
    node.parent=y
    if y is None:
        tree.root=node
    elif node.key<y.key:
        y.left=node
    else:
        y.right=node
        
def inorderTreeWalk(x):
    if x is not None:
        inorderTreeWalk(x.left)
        print(x.key)
        inorderTreeWalk(x.right)
        
def iterTreeSearch(x, k):
    while x is not None and k!=x.key:
        if k<x.key:
            x=x.left
        else:
            x=x.right
    return x
