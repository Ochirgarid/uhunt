import sys

def dig_sum(x):
    if x < 10:
        return x
    s = 0
    while x > 0:
        s += x % 10
        x //= 10

    return dig_sum(s)

def solve(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    s1_sum = 0
    s2_sum = 0
    
    for l in s1:
        if ord('a') <= ord(l) <= ord('z'):
            s1_sum += ord(l) - ord('a') + 1
    
    for l in s2:
        if ord('a') <= ord(l) <= ord('z'):
            s2_sum += ord(l) - ord('a') + 1
    
    s1_sum = dig_sum(s1_sum)
    s2_sum = dig_sum(s2_sum)

    s1_sum, s2_sum = max(s1_sum, s2_sum), min(s1_sum, s2_sum)
    ans = 100.0 * (s2_sum / s1_sum)
    print("{:.2f} %".format(ans) )


if __name__ == "__main__":
    while True:
        name1 = sys.stdin.readline()
        if name1 == '':
            break
        name2 = sys.stdin.readline()

        solve(name1, name2)