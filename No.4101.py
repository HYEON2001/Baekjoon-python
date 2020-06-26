def big(x, y):
    if x == y:
        return "No"
    elif max(x, y) == x:
        return "Yes"
    else:
        return "No"

while True:
    A, B = map(int, input().split())
    if A == 0:
        break
    print(big(A, B))
