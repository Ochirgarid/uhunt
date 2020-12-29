if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        c = int(input())
        ans = -150001
        for i in range(1, n):
            x = int(input())
            ans = max(c - x, ans)
            c = max(c, x)
        print(ans)