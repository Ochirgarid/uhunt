def detect_digit(s, n):
    d = [
        ".*..*..*..*..*.",
        "***..*****..***",
        "***..****..****"
    ]
    ans = 0
    for i in range(0, 4*n, 4):
        ds = "".join([s[j][i:i+3] for j in range(5)])

        ans = ans * 10 + sum([x+1 for x in range(3) if d[x] == ds])

    print(ans)

if __name__ == "__main__":
    n = int(input())
    s = [input().strip() for _ in range(5)]
    detect_digit(s, n)