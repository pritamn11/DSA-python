l1 = [1,2,4,6,10,11,12]
 
low = 0
high = len(l1) - 1
flag = False
while not flag and low <= high:   # until low is less than equal to high, This loop will continue only till then, jab tak low high se chota aur equal to hai tab tak hi chalna warna apna kam rok dena
    mid = (low + high) // 2
    print("Low ",low)
    print("High ",high)
    print("Mid ",mid)
    print(low <= high)
    print(10*"-")
    key = 10
    if key == l1[mid]:
        print("key found at index", mid)
        flag = True
    elif key > l1[mid]:
        low = mid + 1
    else:
        high = mid - 1

  
if not flag:
    print("ELement not exist")

    
