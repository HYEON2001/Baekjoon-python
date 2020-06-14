T = int(input())
for _ in range(T):
    n,s = input().split()
    v = ''
    for i in s:
        v += int(n)*i
    print(v)