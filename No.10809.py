S = input()
lists = [-1] * 26
for i in range(len(S)):
    if lists[ord(S[i]) - 97] != -1:
        pass
    else:
        lists[ord(S[i]) - 97] = i
for i in range(26):
    print(lists[i], end=' ')