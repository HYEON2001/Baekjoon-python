M = int(input())
N = int(input())
lists = []
for i in range(M, N+1):
    cn = 0
    for j in range(1, i+1):
        if i % j == 0:
            cn += 1
            if cn > 2:
               break
    if cn == 2:
        lists.append(i)
if not lists:
    print(-1)
else:
    print(sum(lists))
    print(lists[0])