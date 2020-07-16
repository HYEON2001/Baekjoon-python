import sys
n = int(sys.stdin.readline())
for _ in range(n):
    p = int(sys.stdin.readline())
    l = []
    for _ in range(p):
        a, b = map(str, sys.stdin.readline().split())
        l.append([ int(a), b])
    l = sorted(l, key=lambda x:x[0])
    print(l[-1][1])