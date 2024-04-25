class MyClass:
    def __init__(self, value):
        self.value = value

    def return_self(self):
        if self.value > 10:
            return self
        elif self.value < 10:
            self = None 
        

# Create an instance of MyClass
obj = MyClass(5)

# Call the return_self method, which returns the instance itself
returned_obj = obj.return_self()

# Check if the returned object is the same as the original object
# print(returned_obj is obj)  # Output: True
print(returned_obj)  # Output: True
