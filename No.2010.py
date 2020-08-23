import sys
N = int(sys.stdin.readline())
cn = 0
for i in range(N):
    cn += int(sys.stdin.readline())
print(cn - (N - 1))