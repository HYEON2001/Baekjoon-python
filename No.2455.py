p = []
h = 0
for _ in range(4):
    A, B = map(int, input().split())
    h += B
    h -= A
    p.append(h)

print(max(p))