class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None 
        self.rchild = None 

    def insert(self,data):
        if self.key == None:
            self.key = data
        
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

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild is not None:
            self.lchild.preorder()
        if self.rchild is not None:
            self.rchild.preorder()

    def delete(self, data):
        if self.key is None:
            print("Tree is empty")
            return 
        
        if data < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given node is not present in a Tree")
        elif data > self.key:  
            if self.rchild is not None:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present in a Tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp 


        

root = BST(10)
list1 = [6,3,1,6,98,3,7]  
for i in list1:
    root.insert(i)

root.delete(1)  
root.preorder()

