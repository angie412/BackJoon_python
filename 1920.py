#  이진탐색으로 해보쟘,.,

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def binary_search(value, start, end):
    if start > end :
        return False
    med = (start+end)//2
    if n_list[med] > value :
        return binary_search(value, start, med-1)
    elif n_list[med] < value :
        return binary_search(value, med+1, end)
    else :
        return True
    
for value in m_list :
    if binary_search(value,0, n-1):
        print(1)
    else :
        print(0)
