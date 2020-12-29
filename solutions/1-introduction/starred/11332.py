def dig_sum(x):
    if x < 10:
        return x
    s = 0
    while x > 0:
        s += x % 10
        x //= 10

    return dig_sum(s)

if __name__ == "__main__":
    while True:
        x = int(input())
        if x == 0:
            break
        print(dig_sum(x))
