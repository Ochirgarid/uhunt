def solve(s):
    stack = []
    ans = 0

    for i, l in enumerate(s):
        if l == "\\":
            stack.append(i)
        elif l == "/":
            if stack:
                j = stack.pop()
                ans += i - j

    print(ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve(input().strip())