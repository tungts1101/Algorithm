# implementation for avl tree

class Node:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self,root,x):
        if not root:
            return Node(x)
        elif x < root.val:
            root.left = self.insert(root.left,x)
        else:
            root.right = self.insert(root.right,x)
        
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balance = self.getBalance(root)
        
        # LL
        if balance > 1 and x < root.left.val:
            return self.leftRotate(root)

        # LR
        if balance > 1 and x > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # RR
        if balance < -1 and x > root.right.val:
            return self.rightRotate(root)

        # RL
        if balance < -1 and x < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root
    
    def rightRotate(self,root):
        y = root.left
        T2 = y.right
        
        y.right = root
        root.left = T2

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y
     
    def leftRotate(self,root):
        y = root.right
        T2 = y.left
        
        y.left = root
        root.right = T2

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y
    
    def getHeight(self,root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self,root):
        if not root:
            return
        
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

t = AVLTree()
root = None
root = t.insert(root,10)
root = t.insert(root,5)
root = t.insert(root,20)
root = t.insert(root,4)
root = t.insert(root,14)
root = t.insert(root,16)

t.preOrder(root)

