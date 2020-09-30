S = input().upper()
lists = [0] * 26
for i in S:
    lists[ord(i) - 65] = lists[ord(i) - 65] + 1
c = max(lists)
if lists.count(c) >= 2:
    print('?')
else:
    print(chr(lists.index(c) + 65))