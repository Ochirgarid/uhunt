if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        print("Case #{}:".format(i + 1))
        sites = {}
        max_r = 0
        for _ in range(10):
            s, r = input().split(' ')
            r = int(r)
            sites[r] = sites.get(r, [])
            sites[r].append(s)
            max_r = max(max_r, r)
        for s in sites[max_r]:
            print(s)
        