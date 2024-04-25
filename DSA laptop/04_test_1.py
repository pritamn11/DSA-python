class Parent:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child_name):
        for child in self.children:
            if child.name == child_name:
                self.children.remove(child)
                child.parent = None  # Remove parent reference from child
                child = None  # Set child object to None
                return
        print(f"{child_name} not found in children list.")

    def display_children(self):
        print(f"Children of {self.name}:")
        for child in self.children:
            print(child.name)

class Child:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent
        parent.add_child(self)

# Example usage:
father = Parent("John")
child1 = Child("Alice")
child2 = Child("Bob")
child3 = Child("Charlie")

# Assign parent to children
child1.set_parent(father)
child2.set_parent(father)
child3.set_parent(father)

# Display children before removal
father.display_children()

# Remove a child
father.remove_child("Bob")

# # Display children after removal
father.display_children()
