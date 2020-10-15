cn = 1
while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    print("Triangle #{}".format(cn))
    cn += 1
    if a == -1:
        if c ** 2 - b ** 2 <= 0:
            print("Impossible.\n")
        else:
            print("a = {:.3f}\n".format((c ** 2 - b ** 2) ** 0.5))
    elif b == -1:
        if c ** 2 - a ** 2 <= 0:
            print("Impossible.\n")
        else:
            print("b = {:.3f}\n".format((c ** 2 - a ** 2) ** 0.5))
    else:
        print("c = {:.3f}\n".format((a ** 2 + b ** 2) ** 0.5))
