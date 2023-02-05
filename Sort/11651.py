import sys
input = sys.stdin.readline

N = int(input())
x = []
for i in range(N):
    x.append(list(map(int, input().split())))
xx = sorted(x, key=lambda x: (x[1], x[0]))

for a in xx:
    print(a[0], a[1])