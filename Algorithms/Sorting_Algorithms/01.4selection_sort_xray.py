l1 = [56,3,2,0]

n = len(l1)   # 6

# for i in range(n):
#     print('>>',i,end=" ")
#     for j in range(i+1,n):
#         print('$',j,end=" ")


for i in range(len(l1)):
    min_val = min(l1[i:])
    print("min_val",min_val)
    min_index = l1.index(min_val)
    print("min_index",min_index)
    l1[i], l1[min_index] = l1[min_index], l1[i]
    print(f"l1[{i}]",l1[i])
    print("l1 min_index",l1[min_index])
    print(l1)
    print("-----")
# print(l1)


  

