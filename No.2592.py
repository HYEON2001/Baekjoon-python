lists = []
for i in range(10):
    n = int(input())
    lists.append(n)
print(sum(lists) // 10)
print(max(lists, key=lists.count))