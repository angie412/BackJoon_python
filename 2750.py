n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

nums_sorted = sorted(nums)
# set함수 써서 중복제거 가능
for j in range(len(nums_sorted)):
    print(nums_sorted[j])
