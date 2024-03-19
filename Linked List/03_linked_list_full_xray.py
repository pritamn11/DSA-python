
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None 

class SinglyLinkedList:
    def __init__(self):
        self.head = None 

    def displayLinkedList(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            n = self.head 
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.ref 



sll1 = SinglyLinkedList()
sll1.head = Node(10)
sll2 = Node(20)
sll3 = Node(30)
sll4 = Node(40)

sll1.head.ref = sll2
sll2.ref = sll3
sll3.ref = sll4
# sll4.ref = None


# n = sll1.head    #self.head, Node(10)
# print(n.data)
# n = sll1.head.ref   # sll2, Node(20)
# print(n.data)
# n = sll2.ref   # sll3, Node(30)
# print(n.data)
# n = sll3.ref    # sll4, Node(40)
# print(n.data)
# n = sll4.ref    # Null
# print(n)



# n = sll1.head    #self.head, Node(10)
# print(n.data)
# n = n.ref   # sll2, Node(20)
# print(n.data)
# n = n.ref   # sll3, Node(30)
# print(n.data)
# n = n.ref    # sll4, Node(40)
# print(n.data)
# n = n.ref    # Null
# print(n)



# n = sll1.head    #self.head, Node(10)
# print(n.data)
# n = sll1.head.ref   # sll2, Node(20)
# print(n.data)
# n = sll1.head.ref.ref   # sll3, Node(30)
# print(n.data)
# n = sll1.head.ref.ref.ref    # sll4, Node(40)
# print(n.data)
# n = sll1.head.ref.ref.ref.ref    # Null
# print(n)

