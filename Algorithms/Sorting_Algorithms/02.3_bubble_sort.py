arr = [10,15,4,23,0]

n = len(arr)  #5

for j in range(n-1):
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i] , arr[i+1] = arr[i+1] , arr[i]

print(arr)  # [0, 4, 10, 15, 23]
