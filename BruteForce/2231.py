#  brute: 무식한, force: 힘 무식한 힘으로 해석할 수 있다. 완전탐색 알고리즘.
N = int(input())

def find_b(i, N):
    b = i
    bs = str(b)  
    for i1 in bs:
        b += int(i1)
    if b == N:
        return i
    return 0

cnt = 0
for i in range(N):
    cnt = find_b(i, N)
    if cnt != 0:
        print(cnt)
        break
if cnt == 0:
    print(0)

    

    