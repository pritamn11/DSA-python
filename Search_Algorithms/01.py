
l1 = [1,2,4,6,10,11,3]
key = 4



low = 0
high = len(l1) - 1

flag = False
while not flag:
    mid = low + high // 2
    found = False
    if key == l1[mid]:
        found = True
        print(mid)
    elif key > l1[mid]:
        low = mid + 1
    else:
        high = mid - 1 

    if found == True:
        flag = True
if not found:
    print("Key not exist in list")

