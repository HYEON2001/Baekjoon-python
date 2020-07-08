n = int(input())
cor = {'1': 0, '2': 0, '3': 0, '4': 0, 'axis': 0}
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        cor['axis'] += 1
    elif x > 0 and y > 0:
        cor['1'] += 1
    elif x < 0 and y > 0:
        cor['2'] += 1
    elif x < 0 and y < 0:
        cor['3'] += 1
    elif x > 0 and y < 0:
        cor['4'] += 1
print('{}: {}'.format('Q1', cor['1']))
print('{}: {}'.format('Q2', cor['2']))
print('{}: {}'.format('Q3', cor['3']))
print('{}: {}'.format('Q4', cor['4']))
print("{}: {}".format('AXIS', cor['axis']))