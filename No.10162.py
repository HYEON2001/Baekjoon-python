T = int(input())
a = 0
b = 0
c = 0
if T % 10 != 0:
    print(-1)
else:
    a += T // 300
    T -= 300 * (T // 300)
    b += T // 60
    T -= 60 * (T // 60)
    c += T // 10
    T -= 10 * (T // 10)
    print("{} {} {}".format(a, b, c))
