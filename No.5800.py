K = int(input())
for i in range(K):
    lists = list(map(int, input().split()))
    f = lists[0]
    lists.remove(f)
    M = max(lists)
    m = min(lists)
    lists.sort()
    lists_g = []
    for j in range(f-1):
        lists_g.append(abs(lists[j]-lists[j+1]))
    print("Class {}".format(i+1))
    print("Max {}, Min {}, Largest gap {}".format(M, m, max(lists_g)))
