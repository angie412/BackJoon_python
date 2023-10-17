n_list = []

for _ in range(9):
    n = int(input())
    n_list.append(n)

rem_first=0
rem_second=0

sum_list = sum(n_list)
for i in range(8):
    for j in range(i+1,9):
        if sum_list -(n_list[i]+n_list[j]) == 100:
            rem_first = n_list[i]
            rem_second = n_list[j]

n_list.remove(rem_first)
n_list.remove(rem_second)
n_list.sort()
for i in n_list :
    print(i)

