p = 0
lists = []
for _ in range(10):
    A, B = map(int, input().split())
    p += (B - A)
    lists.append(p)
print(max(lists))