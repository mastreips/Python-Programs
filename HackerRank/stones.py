
n = raw_input()
n2 = int(n)*3
lists = list()
lists2 = list()
[lists.append(int(raw_input())) for _ in range(n2)]

ln = 0
i = 0

while i <= len(lists)-3:
    
    stones = lists[i]-1
    one = lists[i+1]
    two = lists[i+2]
    a = min(one, two)
    b = max(one, two)
    current = a*stones
    maxi = b*stones
    diff = b - a
    if a == b:
        print(current)
    else:
        while current <= maxi:
            lists2.append(current)
            current += diff
        print(' '.join(map(str, lists2)))

    del lists2[:]
    i += 3
