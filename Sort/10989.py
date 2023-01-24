# 전략 인덱스를 수로 생각하고 값에 해당 수가 몇번 들어왔는지 마킹용으로 사용하자
import sys
input = sys.stdin.readline
N = int(input())

# 10000과 같거나 작은 자연수
# 0을 자연수로 처리할 수 있으므로 10001까지 하여 0부터 10000까지 처리할 수 있도록 하였다.
arr = [0] * 10001
for i in range(N):
    num = int(input())
    arr[num] += 1
for a in range(len(arr)):
    if arr[a] != 0:
        for i in range(arr[a]):
            print(a)