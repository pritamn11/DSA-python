
def BinarySearch(list1, key):
    low = 0
    high = len(list1) - 1

    flag = False
    while not flag and low <= high:
        mid = (low + high) // 2

        if key == list1[mid]:
            print("Key found at index", mid)
            flag = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high = mid - 1

        
    if not flag:
        print("Key not exist in list")


l1 = [1,2,4,6,10,11,13]
key = int(input("Enter Key : "))
BinarySearch(l1, key)