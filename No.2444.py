N = int(input())
a = N
for i in range(1, N+1):
    print(" " * (a - i) + "*" * (2 * i - 1))
for j in range(1, N):
    print(" " * j + "*" * (2 * (a - j) - 1))