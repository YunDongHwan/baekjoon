while True:
    N = int(input())
    if N == 0:
        break
    arr = [x for x in range((N * 2) + 1)]
    answer = []
    for a in range(2, (N * 2) + 1):
        if arr[a] != 0:
            if a > N and a <= 2 * N:
                answer.append(a)
            for c in range(a * 2, (N * 2) + 1, a):
                arr[c] = 0
    print(len(answer))
