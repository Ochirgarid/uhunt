import math

def solve(x):
    y = math.floor((2 * x + 0.25) ** 0.5 - 0.5)
    return y

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        print(solve(int(input())))
