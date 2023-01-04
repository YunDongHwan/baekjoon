M = int(input())
N = int(input())
N += 1
arr = [x for x in range(N)]
arr[1] = 0
for a in range(N):
    if arr[a] != 0:        
        for c in range(a * 2, N, a):
            arr[c] = 0
small = 0
sum = 0
for a in range(M, N):
    if arr[a] != 0:
        if sum == 0:
            small = arr[a] 
        sum += arr[a]
if small == 0:
    print(-1)
else:
    print(sum)
    print(small)