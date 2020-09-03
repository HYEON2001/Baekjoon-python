h = []
for _ in range(3):
    hi = int(input())
    h.append(hi)
b = []
for _ in range(2):
    bi = int(input())
    b.append(bi)
print(min(h) + min(b) - 50)