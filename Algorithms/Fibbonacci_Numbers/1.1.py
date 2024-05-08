# n = int(input("enter how many numbers you want in series: "))
n = 5 
first = 0
second = 1

for i in range(n):
    print(first,end=" ")
    temp = first
    first = second 
    second = temp + second
     
