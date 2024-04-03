
def search(list1, key):
    list2 = []
    flag = False
    for i in range(0,len(list1)):
        if key == list1[i]:
            flag = True
            list2.append(i)
    if flag==True:
        for i in list2:
            print("The key is present at index",i)
    else:
        print("Key is not found in list")
        


list1 = [24, 67, 5, 6, 41, 17, 32, 55, 17]
key = int(input("Enter the element: "))

search(list1, key)