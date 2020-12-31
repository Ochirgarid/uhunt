from sys import stdin


if __name__ == "__main__":

    while True:
        s = stdin.readline()
        if s == "":
            break
        n, b, h, w = map(int, s.split())
        hs = []
        av = []
        for _ in range(h):
            hs.append(int(stdin.readline()))
            av.append(list(map(int, stdin.readline().split())))

        cur_min = b + 1
        for hi in range(h):
            for wi in range(w):
                if av[hi][wi] >= n:
                    cur_min = min(cur_min, hs[hi] * n)

        if cur_min == b + 1:
            print("stay home")
        else:
            print(cur_min)