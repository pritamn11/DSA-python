arr = [15,10,1,9,6,14]

n = len(arr)

for j in range(n-1,0,-1):    # we use differnet approach for loop
    for i in range(j):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)


