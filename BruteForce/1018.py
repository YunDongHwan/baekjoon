def findFit(li, i, j):
    cnt = 0
    cnt2 = 0
    s = li[i][j] # 현재 위치를 체스판 시작점으로 선언
    for y in range(i, i + 8):
        for x in range(j, j + 8):
            if (x + y) % 2 == 0:
                if li[y][x] != s:
                    cnt += 1
                else:
                    cnt2 += 1
            else:
                if li[y][x] == s:
                    cnt += 1
                else:
                    cnt2 += 1
    if cnt < cnt2:
        return cnt
    return cnt2

y, x = map(int, input().split())
li = []
for i in range(y):
    str = input()
    li.append(str)

min = findFit(li, 0, 0)
for i in range(y - 7):
    for j in range(x - 7):
        fit = findFit(li, i, j)
        if min > fit:
            min = fit
print(min)