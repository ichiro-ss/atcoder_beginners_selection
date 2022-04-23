# input
s = str(input())

t_words = ["dream", "dreamer", "erase", "eraser"]
t_words = [t_words[i][::-1] for i in range(4)]
reversed_s = s[::-1]
cnt = 0

for i in range(len(s)):
    if i == cnt:
        for j in range(4):
            if reversed_s[i:i+len(t_words[j])] == t_words[j]:
                cnt += len(t_words[j])
                break
if cnt == len(s):
    print("YES")
else:
    print("NO")

# import re; print('YES' if re.search('^(eraser?|dream(er)?)*$',input()) else 'NO')