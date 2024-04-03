arr = [10,15,4,23,0]

n = len(arr)  #5

for i in range(n-1):
    if arr[i] > arr[i+1]:
        arr[i] , arr[i+1] = arr[i+1] , arr[i]

print(arr)   # [10, 4, 15, 0, 23] # this is result of first iteration to get the proper sort
              # we need to iterate it len(arr) -1 times i.e 4 times
        