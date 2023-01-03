A, B = input().split()
A = A[::-1]
B = B[::-1]
LA = list(map(int, A))
LB = list(map(int, B))
gap = len(LA) - len(LB)
if (gap > 0):
    while gap != 0:
        LB.append(0)
        gap -= 1
elif (gap < 0):
    while gap != 0:
        LA.append(0)
        gap += 1
i = 0
answer = []
up = 0
while i < len(LA) or i < len(LB):
    answer.append(up)
    if LA[i] + LB[i] + up >= 10:
        up = 1
    else:
        up = 0
    answer[i] += (LA[i] + LB[i] - (up * 10))
    i += 1
if (up == 1):
    answer.append(1)
answer.reverse()
print(''.join(str(s) for s in answer))