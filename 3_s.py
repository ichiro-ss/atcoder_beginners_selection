# input
n = int(input())
a = [int(i) for i in input().split()]

ans = 100000
for i in range(n):
    cnt = 0
    while not a[i] % 2:
        cnt += 1
        a[i] /= 2
    if ans > cnt:
        ans = cnt

print(ans)