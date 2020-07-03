N = int(input())
c = []
for _ in range(N):
    c.append(int(input()))
a = c.count(1)
b = c.count(0)
if a > b:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")