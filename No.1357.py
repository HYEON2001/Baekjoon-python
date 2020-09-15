X, Y = map(str, input().split())
x = str(int(X[::-1]) + int(Y[::-1]))
print(int(x[::-1]))