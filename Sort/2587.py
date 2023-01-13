import sys
input=sys.stdin.readline

def find(num, arr):
    if len(arr) == 0:
        return 0
    for i in range(len(arr)):
        if arr[i] > num:
            return i
    return len(arr)

arr = []

for i in range(5):
    num = int(input())
    j = find(num, arr)
    arr.insert(j, num)

print(sum(arr) // 5)
print(arr[2])