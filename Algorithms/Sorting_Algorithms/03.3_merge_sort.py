

def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i=0
        j=0
        k=0
        while len(left_list) > i and len(right_list) > j:
            if left_list[i] > right_list[j]:
                list1[k]=right_list[j]
                j+=1
                k+=1
            else:
                list1[k]=left_list[i] 
                i+=1
                k+=1  
        while len(left_list) > i:
            list1[k] = left_list[i]
            i+=1
            k+=1
        while len(right_list) > j:
            list1[k] = right_list[j]
            j+=1
            k+=1    

list1 = [10,5,60,1]
print("Before merge sort",list1)
mergesort(list1)
print("After merge sort ",list1)




