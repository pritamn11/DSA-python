# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# soln : https://medium.com/jen-li-chen-in-data-science/merge-the-tools-4ec999c75bc9


def merge_the_tools(string, k):
    string = string
    k = k
    while string:
        collect_word = ''
        s = string[0:k]
        for i in s:
            if i not in collect_word:
                collect_word += i
        print(collect_word)
        string = string[k:]

if __name__ == '__main__':
    string, k = 'AAABCADDE', 3
    merge_the_tools(string, k)