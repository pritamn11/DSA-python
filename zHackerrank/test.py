string = 'AABCAAADA'
k=3

l = len(string)//k
for i in range(l):
    print(''.join(dict.fromkeys(string[i*k:(i*k)+k])),end="")
