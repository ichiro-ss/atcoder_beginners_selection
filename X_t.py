# input
n = int(input())
t, x, y = [0]*(n+1), [0]*(n+1), [0]*(n+1)
for i in range(n):
    t[i+1], x[i+1], y[i+1] = [int(j) for j in input().split()]

for i in range(n):
    distance = abs(x[i+1] - x[i] + y[i+1] - y[i])
    if distance > t[i+1] - t[i] or (t[i+1] - t[i] - distance) % 2:
        print("No")
        exit()
print("Yes")