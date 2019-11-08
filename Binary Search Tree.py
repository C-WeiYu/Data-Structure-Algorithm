class Node(object):
    def __init__(self,val):
        self.parent = None
        self.left = None
        self.right = None
        self.element=val
    
    def insert(self,data):
        if self.val<data:
            if self.right:
                return self.right.insert(data)
        elif self.val>data:
            if self.left:
                return self.left.insert(data)
        else:
            return False
       
class Binary Tree(object):
    def __init__(self):
        self.root=None
        self.leaf=None
        self.size=None
    
    def insert(self,data):
        if self.root :
            self.root.insert(data)
        else :
            self.root=Node(data)
