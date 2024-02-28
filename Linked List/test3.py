
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
    

    def addEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            # new_node.ref = n.ref
            n.ref = new_node
    

    def addBegin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def addAfter(self, data, x):
        n = self.head 
        while n.ref is not None:
            if n.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node value not exist")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
    def addBefore(self, data, x):
        if self.head is None:
            print("Linked list is empty")
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
                new_node.ref = n.ref 
                n.ref = new_node



sll1 = SinglyLinkedList()
sll1.addEnd(10)
sll1.addEnd(20)
sll1.addEnd(30)
sll1.addEnd(40)
sll1.addBegin(1)
sll1.addBegin(2)
sll1.addAfter(11,1)
sll1.addAfter(11,20)

sll1.addBefore(110,20)
sll1.addBefore(112,4)
sll1.displayLinkedList()
            
