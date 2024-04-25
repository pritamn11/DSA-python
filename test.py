
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None 

    
    def search(self ,data):
        if self.key == data:
            print("Node is found ")
            return
        
        if data < self.key:
            if self.lchild is not None:
                self.lchild.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.rchild is not None:
                self.rchild.search(data)
            else:
                print("Node is not present in tree!")
        

    
    def delete(self, data):
        if self.key is None:
            print("Tree is empty!")
            return
        
        if data < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.delete(data)
            else:
                print("Node is not present")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key 
            self.rchild = self.rchild.delete(node.key)
        return self



root = BST(100)

root.lchild = BST(50)
root.rchild = BST(300)


root.lchild.lchild = BST(10)
root.lchild.rchild = BST(70)

root.rchild.rchild = BST(500)

# print(root.key)
# print(root.lchild.key)
# print(root.lchild.lchild.key)
# print(root.lchild.rchild.key)

root.delete(100)
print(root.key)
