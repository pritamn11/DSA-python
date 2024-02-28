## Adding the element at the begining of the linked list 

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None 


class SinglyLinkedList:
    def __init__(self,head = None):
        self.head = head 
    
    # Traversing through linked list
    def printLinkedList(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            # n = self.head 
            while self.head is not None:
                print("self.head :",self.head)
                print("self.head.data",self.head.data)
                self.head = self.head.ref 
                print("self.head :",self.head)
                print()


    def AddBegin(self,data):
        # print(self.head)   ## already None
        new_node = Node(data)   # 10
        # print(new_node)    # <__main__.Node object at 0x000002605A116900>
        # print(new_node.ref) # None
        new_node.ref = self.head 
        # print(self.head)
        self.head = new_node 
        # print(self.head)   # <__main__.Node object at 0x000002605A116900>
        # print(self.head.data)  # 10
 

sll = SinglyLinkedList()
# print(sll)
sll.AddBegin(10)
sll.AddBegin(20)
sll.AddBegin(30)
sll.printLinkedList()    