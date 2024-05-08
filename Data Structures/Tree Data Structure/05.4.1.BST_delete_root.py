# Why we again write code for deletion of root node, because previously we are delete root node in
# case of whhic have two nodes left & right, what if root node is leaf node or 1 child node.


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


    def delete(self, data, curr):
        if self.key == None:
            print("Tree is empty")
        
        if data < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Node is not found")
        elif data > self.key:
            if self.rchild is not None:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("Node is not found")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key 
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild 
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key 
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild 
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key, curr) 
        return self


def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)
 

 
root = BST(10)    # only one node i.e leaf node
list1 = [3,4]

for i in list1:
    root.insert(i)

# print(count(root))
root.preorder()
print()


if count(root)>1:
    root.delete(10, root.key)
else:
    print("can't perform delete operation")

# root.delete(10, root.key)
print()
root.preorder()


