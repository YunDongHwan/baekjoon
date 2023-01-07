M, N = map(int, input().split())
A = []
B = []
for m in range(M):
    A.append(list(map(int, input().split())))
for m in range(M):
    B.append(list(map(int, input().split())))
for m in range(M):
    for n in range(N):
        print(A[m][n] + B[m][n])
