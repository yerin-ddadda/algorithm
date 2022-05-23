t = int(input())
a = '..#.'
b = '.#.#'
c = '#.'
d = '.#.#'
e = '..#.'
for i in range(t):
    string = input()
    print(a*len(string),'.',sep='')
    print(b*len(string),'.',sep='')
    for k in range(len(string)):
        print(c,string[k],'.',sep='',end="")
    print("#",end="")
    print()
    print(d*len(string),'.',sep='')
    print(e*len(string),'.',sep='')