N = int(input())
o = 0
for _ in range(N):
    s, a = map(int, input().split())
    o += (a % s)
print(o)