c = 0
cl = []
for _ in range(7):
    cn = int(input())
    if cn % 2 == 0:
        pass
    else:
        c += cn
        cl.append(cn)
if c == 0:
    print(-1)
else:
    print(c)
    print(min(cl))