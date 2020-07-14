import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    l = []
    for _ in range(N):
        a, b = map(str, sys.stdin.readline().split())
        l.append([a, int(b)])
    l = sorted(l, key=lambda x:x[1])
    print(l[-1][0])