S = input()
lists = [0] * 26
for i in S:
    lists[ord(i) - 97] = S.count(i)
for i in lists:
    print(i, end=" ")