def X(x, y):
    if y % x == 0:
        return "factor"
    elif x % y == 0:
        return "multiple"
    else:
        return "neither"
while True:
    a, b = map(int, input().split())
    if a == 0:
        break
    n = X(a, b)
    print(n)