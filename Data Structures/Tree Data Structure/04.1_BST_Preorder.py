# pre-order traversal algorithm

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

        
root = BST(10)
list1 = [6,3,1,6,98,3,7]
# list1 = [6,3,1,25,30,62]
for i in list1:
    root.insert(i)

root.preorder()

# https://www.youtube.com/watch?v=MV3nPSok0QQ&list=PLzgPDYo_3xukPJdH6hVQ6Iic7KiJuoA-l&index=45
# https://www.youtube.com/watch?v=MV3nPSok0QQ