class Parent:
    def __init__(self, name):
        self.name = name
        self.childrens = []

    def add_child(self, child):
        self.childrens.append(child)

    def display_children(self):
        print(f"Children of {self.name}:")
        for child in self.childrens:
            print(child.name) 

    def remove_children(self, target_name):
        for child in self.childrens:
            if child.name == target_name:
                self.childrens.remove(child) 
                child.parent = None
                child = None 
                return 
        print(f"{target_name} not found in children list.")



class Child:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent
        parent.add_child(self) 
    

father = Parent("Pritam")
child1 = Child("John")
child2 = Child("Charlie")
child3 = Child("Alice")

child1.set_parent(father)
child2.set_parent(father)
child3.set_parent(father)

father.display_children()
father.remove_children('John')
father.display_children()


