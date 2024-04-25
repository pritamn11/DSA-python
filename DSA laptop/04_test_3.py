
list1 = ['pritam','harry','ishika','kunal']

print(list1)

target_name = 'ishika'

for index in range(len(list1)-1):
    if list1[index] == target_name:
        del list1[index]
     
# list1 = [name for name in list1 if name != target_name]
        
print(list1)

