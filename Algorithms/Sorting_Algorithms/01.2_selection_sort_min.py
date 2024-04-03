arr = [25,1,6]

n = len(arr)

for i in range(n):
    min_index = i 
    for j in range(i+1, n):
        print(f"{arr[j]} < {arr[min_index]} : {arr[j] < arr[min_index]}")
        if arr[j] < arr[min_index]:
            min_index = j
            print(f"min_index = {min_index}")
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(f"arr[{i}] = {arr[i]}")
    print(f"arr[{min_index}] = {arr[min_index]}")
    print(arr)
    print("***************************************")

