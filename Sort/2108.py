import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
li = [int(input()) for _ in range(N)]

li.sort()

many = Counter(li)
print(many)
cnt = many.most_common(2)
print(cnt)
avg = sum(li)/N
print(round(avg))
print(li[(N - 1)//2])
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(li[N - 1] - li[0])
