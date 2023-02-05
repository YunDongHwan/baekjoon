import sys
input=sys.stdin.readline

def recursion(s, l, r, a):
    a[0] = a[0] + 1
    if l >= r:        
        return 1
    elif s[l] != s[r]: 
        return 0
    else: 
        return recursion(s, l + 1, r - 1, a)

N = int(input())
arr = []
for i in range(N):
    s = input().rstrip()
    a = [0]
    print(recursion(s, 0, len(s) - 1, a), a[0])
