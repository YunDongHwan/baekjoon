import sys
input = sys.stdin.readline

N = int(input())
x = [0 for _ in range(N)]
for i in range(N):
    x[i] = list(map(int, input().split()))
x.sort()
for a in x:
    print(a[0], a[1])