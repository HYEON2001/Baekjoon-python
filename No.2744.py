s = list(map(str, input()))
for i in range(len(s)):
    if s[i].islower() == 1:
        s[i] = s[i].upper()
    else:
        s[i] = s[i].lower()
print(''.join(s))