N = int(input())
canvas = [[0] * 100 for i in range(100)]
count = 0
for i in range(N):
    x, y = map(int, input().split())
    for a in range(x, x + 10):
        for b in range(y, y + 10):
            if canvas[a][b] == 0:
                canvas[a][b] = 1
                count += 1
print(count)