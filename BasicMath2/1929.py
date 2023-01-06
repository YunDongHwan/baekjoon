M, N = map(int, input().split())
N += 1
arr = [x for x in range(N)]
arr[1] = 0
answer = []
for a in range(2, N):
    if arr[a] != 0:
        if a >= M and a < N:
            print(a)
        for c in range(a * 2, N, a):
            arr[c] = 0