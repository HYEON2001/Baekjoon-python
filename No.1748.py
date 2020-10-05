N = input()
c = 0
for i in range(len(N) - 1):
    c += 9 * 10 ** i * (i + 1)
print(c +(int(N) - 10 ** (len(N) - 1) + 1) * len(N))