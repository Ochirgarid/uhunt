def solve(h):
    cur = h[0]
    high = 0
    low = 0

    for i in range(1, len(h)):
        if h[i] > cur:
            high += 1
        elif h[i] < cur:
            low += 1
        cur = h[i]
    return high, low

if __name__ == "__main__":
    t = int(input())
    for c in range(t):
        n = int(input())
        h = list(map(int, input().split()))
        high, low = solve(h)
        print("Case {}: {} {}".format(c+1, high, low))