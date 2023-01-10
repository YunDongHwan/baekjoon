def quick_sort(array, start, end):
    if start >= end: return 
    pivot = start
    left, right = start + 1, end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
# riget 기준으로 start, end 를 정하는 이유는 pivot이 0번째 인덱스로 시작하여 end로 증가하기 때문에 
# 만약 left로 start, end를 정하면 제일 큰 수가 pivot으로 됐을 때 range error발행
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
quick_sort(arr, 0, N - 1)
for i in arr:
    print(i)