n=0
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    n += a
print("%g"%(n/5))