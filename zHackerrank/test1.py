string = 'AABCAAADA'
k=3


while string:
    collect_word = ''
    s = string[0:k]
    for i in s:
        if i not in collect_word:
            collect_word += i
    print(collect_word)
    string = string[k:]
    



