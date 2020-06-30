import sys
s = sys.stdin.readline()
f = 0.0
if s[0] == 'A':
    f += 4.0
elif s[0] == 'B':
    f += 3.0
elif s[0] == 'C':
    f += 2.0
elif s[0] == 'D':
    f += 1.0
if s[1] == '+':
    f += 0.3
elif s[1] == '-':
    f -= 0.3
print(f)