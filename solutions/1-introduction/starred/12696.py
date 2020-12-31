def check_baggage(l, wi, d, we):
    #length 56cm
    #width 45cm 
    #depth 25cm
    #sum 125cm
    #weight 7kg
    if we > 7.0:
        return False
    if (l <= 56.0 and wi <= 45.0 and d <= 25.0) or l + wi + d <= 125.0:
        return True
    return False


if __name__ == "__main__":
    t = int(input())
    ans = 0
    for _ in range(t):
        if check_baggage(*map(float, input().split())):
            print(1)
            ans += 1
        else:
            print(0)
    print(ans)