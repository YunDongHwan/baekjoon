from dataclasses import dataclass
@dataclass
class MaxNum:
    x: int = 0
    y: int = 0
    max: int = 0
N = []
MN = MaxNum()
for a in range(9):
    N.append(list(map(int, input().split())))
for n in range(len(N)):
    for a in range(len(N[n])):
        if MN.max <= N[a][n]:
            MN.x = n + 1
            MN.y = a + 1
            MN.max = N[a][n]
print(MN.max)
print(MN.y, MN.x)