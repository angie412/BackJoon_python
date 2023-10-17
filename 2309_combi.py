#  combi 표준 라이브러리 이용

import itertools

num_list = [int(input()) for _ in range(9)]

for i in itertools.combinations(num_list,7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break