N = int(input())

cnt = 0
target = 665

while cnt != N:
    target += 1
    is_death = target
    while is_death != 0:
        if is_death % 1000 == 666:
            cnt += 1
            break
        else:
            is_death //= 10
print(target)