T = int(input())
def Max_n(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i ==0:
            return i
        i -= 1
for _ in range(T):
    A, B = map(int, input().split())
    max_n = Max_n(A, B)
    min_n = max_n * (A // max_n) * (B // max_n)
    print(min_n)