x, y = map(int, input().split())
lists = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if x == 1:
    d = y
else:
    d = sum(lists[0:(x - 1)]) + y
day = d % 7
if day == 1:
    print("MON")
elif day == 2:
    print("TUE")
elif day == 3:
    print("WED")
elif day == 4:
    print("THU")
elif day == 5:
    print("FRI")
elif day == 6:
    print("SAT")
elif day == 0:
    print("SUN")
