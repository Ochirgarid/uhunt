from sys import stdin

for s in stdin:
    a, b = map(int, s.split())
    print(2 * a * b)