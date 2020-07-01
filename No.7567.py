import sys
x = str(sys.stdin.readline())
l = len(x)
n = 10
for i in range(l-2):
    if x[i] == x[i+1]:
        n += 5
    elif x[i] != x[i+1]:
        n += 10
print(n)