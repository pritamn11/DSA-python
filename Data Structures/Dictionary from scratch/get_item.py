
# class Test(object):

#     def __getitem__(self, items):
#         print(type(items), items)


# test = Test()
# test[5]
# test[6:23:34]
# test['hello world']
# test[[1,3,4]]
# test[{'a':1}]
# test[object()]

# *************************************************

# class Student:
#     def __init__(self, names):
#         self.names = names

#     def __getitem__(self, index):
#         return self.names[index]

# obj = Student(['A','B','C'])
# print(obj[2])   # C


# *************************************************

# class Mylist:
#     def __init__(self, items):
#         self.items = items

#     def __getitem__(self, index):
#         if isinstance(index, int):
#             return self.items[index]
#         elif isinstance(index, str):
#             return self.items.index(index)
#         else:
#             raise TypeError("Invalid argument type")

# my_list = Mylist(['John','Harry','Jack','Peter'])

# print(my_list[0])    # John
# print(my_list[2])    # Jack  
# print(my_list['Jack'])   # 2
# print(my_list['John'])   # 0



# ****************************************************

import copy

# Constants that can be used to index date of birth's Date-Month-Year
D = 0; M = 1; Y = -1

class Person(object):
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob

    def __getitem__(self, indx):
        print ("Calling __getitem__")
        p = copy.copy(self)

        p.name = p.name.split(" ")[indx]
        p.dob = p.dob[indx] # or, p.dob = p.dob.__getitem__(indx)
        return p
    
p = Person(name='Pritam Narwade',age=20,dob=(11,9,2000))
print(p[0].name)
print(p[Y].age)