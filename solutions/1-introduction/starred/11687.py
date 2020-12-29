if __name__ == "__main__":
    while True:
        x = input()
        if x == "END":
            break
        i = 0
        while str(x) != "1":
            x = len(str(x))
            i += 1
        print(i+1)
