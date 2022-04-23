# input
n = int(input())
a = [int(i) for i in input().split()]

ans = 0
a.sort(reverse = True)
for i in range(n):
    if i % 2:
        ans -= a[i]
    else:
        ans += a[i]

print(ans)