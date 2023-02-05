def merge_sort(a, s, e):
    if s < e:
        p = (e + s) // 2
        merge_sort(a, s, p)
        merge_sort(a, p + 1, e)
        merge(a, s, p, e)
        


def merge(a, s, p, e):
    global cnt
    global ret
    if cnt <= 0:
        return
    i = s
    j = p + 1
    temp = []    
    while i <= p and j <= e:
        if a[i] <= a[j]:            
            temp.append(a[i])
            i += 1
        else:            
            temp.append(a[j])
            j += 1
        cnt -= 1
        if cnt == 0:
            ret = temp[-1]
    while i <= p:
        temp.append(a[i])
        i += 1
        cnt -= 1
        if cnt == 0:
            ret = temp[-1]
    while j <= e:
        temp.append(a[j])
        j += 1
        cnt -= 1
        if cnt == 0:
            ret = temp[-1]
    for i in range(len(temp)):
        a[s + i] = temp[i]


N, K = map(int, input().split())
a = list(map(int, input().split()))
global cnt
global ret
cnt = K
ret = -1
merge_sort(a, 0, N - 1)
print(ret)
