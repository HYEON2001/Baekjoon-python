T = int(input())
for _ in range(T):
    N = int(input())
    a = 0
    b = 0
    for _ in range(N):
        C, G = map(float, input().split())
        a += C
        b += C * G
    print(int(a), '%.1f' % (b/a))