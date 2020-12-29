if __name__ == "__main__":
    while True:
        b, n = map(int, input().split())
        if b + n == 0:
            break
        rl = list(map(int, input().split()))
        r = {(i+1):x for i, x in enumerate(rl)}
        for _ in range(n):
            d, c, v = map(int, input().split())
            r[d] -= v
            r[c] += v

        for v in r.values():
            if v < 0:
                break
        else:
            print("N")
            continue
        print("S")