# input
n = int(input())
d = []
for _ in range(n):
    d.append(int(input()))

size = set()
for i in range(n):
    if not d[i] in size:
        size.add(d[i])
    
print(len(size))