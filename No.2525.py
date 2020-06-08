A, B = input().split()
C = int(input())
A = int(A)
B = int(B)
time = A*60 +B
time = time +C
if time >=1440:
    time-=1440
print("{} {}".format(time//60,time% 60))
