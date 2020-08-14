import sys
n = int(sys.stdin.readline())
f = [0, 1]

if n in (0, 1):
    fi = n
else:
    for _ in range(2, n+1):
        fi = sum(f)
        f = [f[1], fi]
print(fi)