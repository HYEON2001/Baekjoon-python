import math
import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
l = []
c = 0
for i in range(M, N+1):
    s = math.sqrt(i)
    if (s).is_integer() == 1:
        l.append(i)
    else:
        pass
for w in range(len(l)):
    c += l[w]
if len(l) == 0:
    print(-1)
else:
    print(c)
    print(l[0])