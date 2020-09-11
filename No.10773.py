K = int(input())
lists = []
for _ in range(K):
    cn = int(input())
    if cn == 0:
        lists.pop()
    else:
        lists.append(cn)
print(sum(lists))