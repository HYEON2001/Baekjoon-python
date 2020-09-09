lists = []
for _ in range(5):
    lists.append(int(input()))
print(sum(lists) // 5)
lists.sort()
print(lists[2])