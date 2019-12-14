from bstree import *

class RBNode(Node):
    def __init__(self, key, data):
        super().__init__(key, data)
        self.color=True #False for black, true for red
        self.value=None
        
class RBTree(BST):
    def __init__(self):
         super().__init__()
    
    def RBInsert(self, node):
        y=None
        x=self.root
        while x!=None:
            y=x
            if node.key<x.key:
                x=x.left
            else:
                x=x.right
        node.parent=y
        if y is None:
            node.color=False
            self.root=node
            return
        elif node.key<y.key:
            y.left=node
        else:
            y.right=node
        self.RBFix(node)
        self.root.color=False
    
    def RBFix(self, node):
        while node!=self.root and node.parent.color==True and node.parent.parent is not None:
            if node.parent==node.parent.parent.left:
                y=node.parent.parent.right
                if y!=None and y.color==True:
                    node.parent.color=False
                    y.color=False
                    node.parent.parent.color=True
                    node=node.parent.parent
                else:
                    if node == node.parent.right:
                        node=node.parent
                        self.leftRotate(node)
                    node.parent.color=False
                    node.parent.parent.color=True
                    self.rightRotate(node.parent.parent)
            else:
                y=node.parent.parent.left
                if y!=None and y.color==True:
                    node.parent.color=False
                    y.color=False
                    node.parent.parent.color=True
                    self.rightRotate(node.parent.parent)
                else:
                    if node == node.parent.left:
                        node=node.parent
                        self.rightRotate(node)
                    node.parent.color=False
                    node.parent.parent.color=True
                    self.leftRotate(node.parent.parent)
                
    
    def leftRotate(self, node):
        y=node.right
        node.right=y.left
        if y.left!=None:
            y.left.parent=node
        y.parent=node.parent
        if node.parent == None:
            self.root=y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y
        
    def rightRotate(self, node):
        y=node.left
        node.left=y.right
        if y.right!=None:
            y.right.parent=node
        y.parent=node.parent
        if node.parent == None:
            self.root=y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y
    
