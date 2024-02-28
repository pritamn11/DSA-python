# https://www.linkedin.com/pulse/exploring-world-singly-linked-lists-python-data-fiona-githaiga/

class Node:
    def __init__(self, item_name):
        self.item_name = item_name
        self.next_item = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, item_name):
        new_item = Node(item_name)
        if not self.head:
            self.head = new_item
        else:
            current_item = self.head
            while current_item.next_item:
                current_item = current_item.next_item
            current_item.next_item = new_item

    def traverse(self):
        current_item = self.head
        while current_item:
            print(f"{current_item.item_name} -->",end=" ")
            current_item = current_item.next_item

# Example usage
shopping_list = SinglyLinkedList()
shopping_list.add_item("10")
shopping_list.add_item("20")
shopping_list.add_item("30")
shopping_list.add_item("40")

shopping_list.traverse()


