n = int(input())

for i in range(n):
    j, s = input().split()
    j = int(j)
    s = str(s)
    for i in range(len(s)):
        print(j * s[i], end="")
    print()


