# input
n, a, b = [int(i) for i in input().split()]

ans = 0
for i in range(1, n + 1):
    sum_dig = 0 # sum of digits
    num = i
    while num:
        dig = num % 10  # a digit
        sum_dig += dig
        num //= 10
    if a <= sum_dig <= b:
        ans += i

print(ans)

# print(sum(i * (A <= sum(map(int, str(i)))<=B) for i in range(N+1)))