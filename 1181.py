# 중복 제거, 아스키

n = int(input())
str_list = []

for s in range(n):
    str_list.append(input().strip())

set_str = list(set(str_list))

sort_str = []
for s in set_str:
    sort_str.append((len(s),s))

result  = sorted(sort_str)

for s in result:
    print(s[1])


