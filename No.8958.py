n = int(input())
for _ in range(n):
    p = 0
    e = 0
    w = input()
    s = len(w)
    for i in range(s):
        if w[i] == 'O':
            e += 1
            p += e
        elif w[i] == 'X':
            e = 0
    print(p)