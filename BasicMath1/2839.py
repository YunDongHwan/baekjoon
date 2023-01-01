N = int(input())
i = 0
while (N - (3 * i)) > 0 and (N - (3 * i)) % 5 != 0:
    i += 1
print((N - (3 * i)) % 5, i)
if N - (3 * i) < 0:
    print(-1)
else:
    print(int(((N - (3 * i)) / 5) + i))
