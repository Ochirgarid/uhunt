if __name__ == "__main__":
    case = 0
    while True:
        t = input().strip()
        if t == "#":
            break
        case += 1
        if t == "HELLO":
            print("Case {}: ENGLISH".format(case))
        elif t == "HOLA":
            print("Case {}: SPANISH".format(case))
        elif t == "HALLO":
            print("Case {}: GERMAN".format(case))
        elif t == "BONJOUR":
            print("Case {}: FRENCH".format(case))
        elif t == "CIAO":
            print("Case {}: ITALIAN".format(case))
        elif t == "ZDRAVSTVUJTE":
            print("Case {}: RUSSIAN".format(case))
        else:
            print("Case {}: UNKNOWN".format(case))

        