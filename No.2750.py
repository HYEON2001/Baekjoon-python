N = int(input())
lists = []
for _ in range(N):
    cn = int(input())
    lists.append(cn)
lists = sorted(lists)
for i in range(N):
    print(lists[i])
