
class Node:
    def __init__(self, data):
        self.data = data 
        self.ref = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def displayLinkedList(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head 
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref

    def addEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref 
            n.ref = new_node 
    
    def addBegin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def addAfter(self,data,x):
        n = self.head 
        while n is not None:
            if n.data == x:
                break
            n = n.ref 
        if n is None:
            print("Node not Exist")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def addBefore(self,data,x):
        if self.head is None:
            print("Linked List is empty")
            return 
        elif self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref 
            if n.ref is None:
                print("Node value not exist")
            else:
                new_node = Node(data)
                new_node.ref =  n.ref
                n.ref = new_node


    def insertEmpty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    
    def deleteBegin(self):
        if self.head is None:
            print("Linked List is already empty cannot delete nodes")
        else:
            self.head = self.head.ref
        



sll = SinglyLinkedList()
sll.addEnd(10)
sll.addEnd(20)
sll.addEnd(30)
sll.deleteBegin()
sll.displayLinkedList()
