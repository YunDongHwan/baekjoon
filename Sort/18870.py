import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

sortarr = sorted(list(set(arr)))
dic = {sortarr[l] : l for l in range(len(sortarr))}
for a in arr:
    print(dic[a])