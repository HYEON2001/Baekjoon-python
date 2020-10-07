A, B = map(str, input().split())
X = 0
Y = 0
for i in range(len(A)):
    X += int(A[i])
for j in range(len(B)):
    Y += int(B[j])
print(X * Y)
