

class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self, data):
        if self.key == None:
            self.key = data 
            return 
        
        if data == self.key:
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



    def search(self, data):
        if self.key == data:
            print("Node is found")
            return
        
        if data < self.key:
            if self.lchild is not None:
                self.lchild.search(data)
            else:
                print("Node is not present is tree")
        else:
            if self.rchild is not None:
                self.rchild.search(data)
            else:
                print("Node is not present in tree")

    
    def pre_order(self):
        print(self.key, end=" ")
        if self.lchild is not None:
            self.lchild.pre_order()
        if self.rchild is not None:
            self.rchild.pre_order()


 
root = BST(10)
list1 = [6,3,1,6,98,3,7]
for i in list1:
    root.insert(i)


root.pre_order()
