for _ in range(int(input())):
    ans, i = 0, 0
    n, p = map(int, input().split())
    arr = sorted(list(map(int, input().split())))

    for i in arr:
        if i <= p:
            p -= i
            ans += 1

    print(ans)
