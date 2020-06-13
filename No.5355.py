A = int(input())
for i in range(A):
    i = list(map(str,input().split()))
    l=0
    for w in range(len(i)):
        if w == 0:
            l += float(i[w])
        else:
            if i[w] == '@':
                l *= 3
            elif i[w] == '#':
                l -= 7
            elif i[w] == '%':
                l += 5
    print("%0.2f"%l)