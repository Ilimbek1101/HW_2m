#ExtraTask:
# Найди ту единственную.

nums = [8, 2, 3, 3, 8, 5, 2]

for i in nums:
    s = 0
    for k in nums:
        if k == i:
            s += 1
    if s == 1:
        print(i)


