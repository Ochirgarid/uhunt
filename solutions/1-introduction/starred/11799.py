if __name__ == "__main__":
    t = int(input())
    for c in range(t):
        h = list(map(int, input().split()[1:]))
        print("Case {}: {}".format(c+1, max(h)))