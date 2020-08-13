N = input().split()
c = 0
for i in range(5):
    c += int(N[i]) ** 2
print(c % 10)