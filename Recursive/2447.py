import sys
input=sys.stdin.readline
def Draw(N):
    if N == 1:
        return ["*"]
    patern = Draw(N // 3)
    
    board = []
    for p in patern:
        board.append(p * 3)
    for p in patern:
        board.append(p + " " * (N // 3) + p)
    for p in patern:
        board.append(p * 3)
    return board

N = int(input())
board = Draw(N)
print(board)
print("\n".join(board))