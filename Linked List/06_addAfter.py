
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
    


sll = SinglyLinkedList()
sll.addEnd(10)
sll.addEnd(20)
sll.addBegin(50)
sll.addEnd(30)
sll.addBegin(60)
sll.addAfter(11,20)
sll.addAfter(11,60)
sll.displayLinkedList()

