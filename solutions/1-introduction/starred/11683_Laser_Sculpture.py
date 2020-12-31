from sys import stdin

def solve(s, height):
    ans = 0
    prev = 0
    for x in s:
        h = height - x
        if h > prev:
            ans += h - prev
        prev = h
    print(ans)

if __name__ == "__main__":

    while True:
        s = stdin.readline()
        if s[0] == "0": break
        height, _ = map(int, s.split())
        final_shape = list(map(int, stdin.readline().split()))
        solve(final_shape, height)

