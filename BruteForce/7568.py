N = int(input())

def checkBig(b, f):
    if b[0] < f[0] and b[1] < f[1]:
        return 1
    return 0

li = [0 for _ in range(N)]

for n in range(N):
    li[n] = tuple(map(int, input().split()))

for n in range(N):
    cnt = 1
    for l in li:                
        cnt += checkBig(li[n], l)
    print(cnt)