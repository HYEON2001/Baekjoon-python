T = int(input())
for _ in range(T):
    lists = list(map(int, input().split()))
    E = []
    for i in lists:
        if i % 2 == 0:
            E.append(i)
    print(sum(E), min(E))