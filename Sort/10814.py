N = int(input())
li = []
for _ in range(N):
    li.append(tuple(input().split()))
sort = sorted(li, key = lambda age : int(age[0]))
for i in sort:
    print(i[0], i[1])