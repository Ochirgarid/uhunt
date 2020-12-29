from math import ceil

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        print(ceil((a - 2) / 3.0) * ceil((b - 2) / 3.0))