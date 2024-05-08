
list1 = [0,1]
n = 5
for i in range(n):
    next_num = list1[-1] + list1[-2]
    list1.append(next_num)

print(list1[:n])

