t = int(input())
for _ in range(t):
    s = input()
    ans = 0
    cur = 0
    for l in s:
        if l == "O":
            cur += 1
            ans += cur
        else:
            cur = 0
    print(ans)