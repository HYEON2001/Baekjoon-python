n = int(input())
a = 0
b = 1
c = 0
for _ in range(n):
    c = a
    a = b
    b = c + b
print(a)