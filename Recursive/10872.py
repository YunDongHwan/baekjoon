def factor(N):
    if N > 1:
        return N * factor(N - 1)
    return 1

N = int(input())
print(factor(N))
