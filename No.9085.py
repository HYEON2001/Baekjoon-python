T = int(input())
for _ in range(T):
    cnt = 0
    N = int(input())
    n = input().split()
    for i in range(N):
        cnt += int(n[i])
    print(cnt)