
def quadratic_time_function(arr):
    n = len(arr)
    result = 0
    for i in range(n):
        for j in range(n):
            result += arr[i] * arr[j]
    return result


arr = [1,2,3,4,5]

print(quadratic_time_function(arr))
 
 