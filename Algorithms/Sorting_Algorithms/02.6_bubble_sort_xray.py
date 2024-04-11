
arr = [25,1,6,12]
# num = int (input ("how many number you want to enter:"))
# print ("enter values:")
# for k in range (num) :
#     arr.append(int(input()))

# print ("unsorted list:",arr)


for j in range (len(arr)-1,0,-1) :
    for i in range(j):
        if arr[i] > arr[i+1]:
            arr[i], arr [i+1] = arr [i+1], arr[i]
            print (arr)
        else:
            print (arr)
    print ()

print ("sorted list:",arr)