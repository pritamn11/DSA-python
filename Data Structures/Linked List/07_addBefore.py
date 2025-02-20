
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
    
    def addBefore(self,data,x):    # new_data before which element
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


sll = SinglyLinkedList()
sll.addEnd(10)
sll.addEnd(120)
sll.addEnd(23)
sll.addEnd(30)
sll.addBegin(60)

sll.addBefore(120,50) 
sll.addBefore(130,60) 
sll.addBefore(11,23) 
sll.displayLinkedList()

