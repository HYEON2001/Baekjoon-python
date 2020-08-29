T = int(input())
for _ in range(T):
    A, B = map(str, input().split())
    A = int(A)
    B = list(B)
    del B[A - 1]
    print(''.join(B))