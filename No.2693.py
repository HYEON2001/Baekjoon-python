T = int(input())
for _ in range(T):
    lists = list(map(int, input().split()))
    lists.sort(reverse=True)
    print(lists[2])
