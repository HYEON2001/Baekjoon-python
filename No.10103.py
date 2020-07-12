n = int(input())
s1 = 100
s2 = 100
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        s2 -= a
    elif a < b:
        s1 -= b
    elif a == b:
        pass
print(s1)
print(s2)