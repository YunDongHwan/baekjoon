N, M = map(int, input().split())
S = list()
count = 0
for _ in range(N):
    S.append(input())
for _ in range(M):
    c = input()
    if c in S:
        count += 1
print(count)
