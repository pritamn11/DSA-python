list1 = [20,1,5,40,10]

def mergesort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        mergesort(left_list)
        mergesort(right_list)
        print("L",left_list)
        # print("R",right_list)
        i=0
        j=0
        k=0
        # print("len L",len(left_list))
        # print("len R",len(right_list))


mergesort(list1)
