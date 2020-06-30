import sys
A, B = map(int, sys.stdin.readline().split())
t = 60 * A + B
if t >= 1440:
    t -= 1440
    t -= 45
elif t - 45 < 0:
    t = 1440 - (45 - t)
else:
    t -= 45
print("{} {}".format((t//60), (t % 60)))