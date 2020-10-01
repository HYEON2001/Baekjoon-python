T = int(input())
for _ in range(T):
    A, B = map(str, input().split())
    d = []
    for i in range(len(A)):
        if ord(A[i]) > ord(B[i]):
            d.append(str(abs(ord(B[i]) - ord(A[i]) + 26)))
        elif ord(A[i]) <= ord(B[i]):
            d.append(str(abs(ord(A[i]) - ord(B[i]))))
    print("Distances: {}".format(' '.join(d)))
