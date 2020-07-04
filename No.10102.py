V = int(input())
s = str(input())
a = s.count('A')
b = s.count('B')
if a > b:
    print('A')
elif a < b:
    print('B')
elif a == b:
    print('Tie')
