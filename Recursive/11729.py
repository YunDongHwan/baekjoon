import math

MSG_FORMAT = "{} {}"

N = int(input())


def move(start, to):
    print(MSG_FORMAT.format(start, to))

def hanoi(pan, start, to, via):
    if pan == 1:
        move(start, to)
        return
    hanoi(pan - 1, start, via, to)
    move(start, to)
    hanoi(pan - 1, via, to, start)

print(int(math.pow(2, N) - 1))
hanoi(N, 1, 3, 2)