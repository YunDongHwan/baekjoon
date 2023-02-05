N = int(input())
d = {}
for n in range(N):
    i = input()
    d[i] = len(i)
sort = sorted(d.items(), key=lambda num : (num[1], num[0]))
for i in sort:
    print(i[0])
