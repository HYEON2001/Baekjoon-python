N = int(input())
M = []
for _ in range(N):
    A, B, C = map(int, input().split())

    if A == B == C:
        M.append(10000 + A * 1000)
    elif A == B:
        M.append(1000 + A * 100)
    elif A == C:
        M.append(1000 + A * 100)
    elif B == C:
        M.append(1000 + B * 100)
    else:
        M.append(max(A, B, C) * 100)

print(max(M))