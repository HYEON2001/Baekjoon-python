T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    c = 0
    for i in range(N, M+1):
        if str(i).count('0') != 0:
            c += str(i).count('0')
    print(c)