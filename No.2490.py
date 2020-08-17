for _ in range(3):
    y = list(map(int, input().split()))
    if y.count(1) == 0:
        print("D")
    elif y.count(1) == 2:
        print("B")
    elif y.count(1) == 1:
        print("C")
    elif y.count(1) == 3:
        print("A")
    elif y.count(1) == 4:
        print("E")