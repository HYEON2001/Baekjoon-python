n = []
for _ in range(9):
    n.append(int(input()))
lie_1 = 0
lie_2 = 0
for i in range(8):
    for j in range(i+1, 9):
        if sum(n) - 100 == n[i] + n[j]:
            lie_1 = n[i]
            lie_2 = n[j]
n.remove(lie_1)
n.remove(lie_2)
for i in n:
    print(i)