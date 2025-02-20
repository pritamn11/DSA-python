class Person:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    
    def show_child(self):
        for i in self.children:
            print(i.name)

    def search(self, target_name):     # self yaha pr father hai
        if self.name == target_name:
            print("Found")
            return 
        for child in self.children:
            if child.search(target_name):
                print("Found")
                return
        print("Not Found")
        


# Example usage:
father = Person("John")
mother = Person("Mary")
child1 = Person("Alice")
child2 = Person("Bob")

father.add_child(child1)
father.add_child(child2)
father.add_child(mother)

father.show_child()

(father.search("Bob"))
# (father.search("Harry"))
# print(father.search("Mary"))
# print(father.search("Mike"))

# print("Search for 'Alice':", father.search("Alice"))  # Output: True
# print("Search for 'David':", father.search("David"))  # Output: False
