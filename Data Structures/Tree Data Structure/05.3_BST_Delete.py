# Delete . https://www.youtube.com/watch?v=kDbqMBgVr9s&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=49

class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key == None:
            self.key = data
            return
        
        if self.key == data:
            return
        
        if data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
        else:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)


    def search(self, data):
        if self.key == data:
            print("Node is found!")
            return
         
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in tree!")

    
    def preorder(self):
        print(self.key,end=" ")
        if self.lchild is not None:
            self.lchild.preorder()
        if self.rchild is not None:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild is not None:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild is not None:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild is not None:
            self.lchild.postorder()
        if self.rchild is not None:
            self.rchild.postorder()
        print(self.key,end=" ")


    def delete(self, data):
        if self.key == None:
            print("Tree is empty")
        
        if data < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.delete(data)
            else:
                print("Node is not found")
        elif data > self.key:
            if self.rchild is not None:
                self.rchild = self.rchild.delete(data)
            else:
                print("Node is not found")
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


 
root = BST(10)
# list1 = [6,3,1,6,98,95,100,3,7]
list1 = [6,3,1,6,3,7,98]

for i in list1:
    root.insert(i)

# root.inorder()

root.delete(10)
print()
# print(root.key)
root.inorder()


# if the delete method is designed to return the updated tree after deleting a node, 
# then assigning self.lchild = self.lchild.delete(data) ensures that the changes are 
# reflected in the tree structure. If you don't assign it back, the changes won't be 
# captured, and you won't see the effect of the deletion operation on the tree structure.

