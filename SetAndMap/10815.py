import sys
input = sys.stdin.readline

N = int(input())
sn = list(map(int, input().split()))
dic = {}
for s in sn:
    dic[s] = 1
C = int(input())
cn = list(map(int, input().split()))
for a in cn:
    if dic.get(a) == 1:
        print(1)
    else:
        print(0)
