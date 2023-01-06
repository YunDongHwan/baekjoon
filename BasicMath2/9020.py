def isSosu(n):
    if n != 1:
        for a in range(2, n + 1):
            if n % a == 0 and a != n:
                return False
            elif a == n:
                return True
T = int(input())
for t in range(T):
    N = int(input())
    pibot = N // 2
    for p in range(N):
        if isSosu(pibot) == True and (isSosu(N - pibot)) == True:
            print(pibot, N - pibot)
            break
        else:
            pibot -= 1
