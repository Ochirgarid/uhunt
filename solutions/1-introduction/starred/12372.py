if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        a, b, c = map(int, input().split())
        print("Case {}: ".format(i + 1), end="")
        print("good" if a <= 20 and b <= 20 and c <= 20 else "bad")