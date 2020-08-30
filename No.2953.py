m = 0
mi = 0
for i in range(1, 6):
    N = sum(list(map(int, input().split())))
    if N > m:
        m = N
        mi = i
print(mi, m)
