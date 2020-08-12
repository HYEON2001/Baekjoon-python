l = []
for _ in range(9):
    c = int(input())
    l.append(c)
m = max(l)
lm = l.index(m)
print(m)
print(lm+1)