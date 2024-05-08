list1 = [67,78,45,23,89,34,3]

n = len(list1)

min = list1[0]

for i in list1:
    if i < min:
        min = i 
print(min)