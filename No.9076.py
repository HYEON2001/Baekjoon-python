T = int(input())
for _ in range(T):
    lists = list(map(int, input().split()))
    lists.remove(max(lists))
    lists.remove(min(lists))
    if max(lists) - min(lists) >= 4:
        print("KIN")
    else:
        print(sum(lists))