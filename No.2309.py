l = []
for _ in range(9):
    l.append(int(input()))
s = sum(l)
lie_1 = 0
lie_2 = 0
for i in range(8):
    for j in range(i+1, 9):
        if s - (l[i] + l[j]) == 100:
            lie_1 = l[i]
            lie_2 = l[j]
l.remove(lie_1)
l.remove(lie_2)
l = sorted(l)
for i in l:
    print(i)