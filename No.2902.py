s = input()
lists = []
lists.append(s[0])
for i in range(len(s)):
    if s[i] == '-':
        lists.append(s[i+1])
print(''.join(lists))