N = int(input())
sc = list(map(int, input().split()))
M = max(sc)
Ml = []
for i in range(N):
    Ml.append((sc[i] / M) * 100)
avg = sum(Ml) / N
print(avg)