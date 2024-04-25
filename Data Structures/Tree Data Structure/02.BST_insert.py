
class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None 
        self.rchild = None 

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:
            return 
        
        if data < self.key:
            if self.lchild is not None:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild is not None:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)


root = BST(10)
list1 = [6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)
    



