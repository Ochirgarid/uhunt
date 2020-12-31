if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        cur = 0
        m = []
        for i in range(n):
            s = input().strip()
            if " " in s:
                x = int(s.split(" ")[-1]) - 1
                cur += m[x]
                m.append(m[x])
            elif s == "LEFT":
                m.append(-1)
                cur -= 1
            else:
                m.append(1)
                cur += 1

        print(cur)