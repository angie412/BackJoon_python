#  가져갈수 있는 최대높이 -> 이분탐색으로 hegith 



n,m = map(int,input().split())

n_list = list(map(int, input().split()))
# list 입력 받을시 

def find_cut_tree(height):
    total_heigth = 0
    for tree in n_list :
        if tree > height:
            total_heigth += (tree - height)
    return total_heigth


start = 0
end = (max(n_list))
result = 0


# while

while start <= end :
    midean = (start + end) //2
    cut_height = find_cut_tree(midean)

    if cut_height >= m :
        result = midean
        start = midean + 1
    else :
        end = midean -1
    
print(result)