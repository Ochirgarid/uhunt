case = 0
while True:
    t = int(input())
    if t == 0:
        break

    e = list(map(int, input().strip().split()))
    m, z = 0, 0
    for x in e:
        if x > 0:
            m += 1
        else:
            z += 1
    case += 1
    print("Case {}: {}".format(case, m - z))