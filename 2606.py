# def dfs(dd):
#     count = 0
#     visited[dd]
# node1, node2 -> 처음엔 마지막 node6의 값 담겨있음 
cnt = 0
def dfs(dd):
    global cnt
    visited[dd] = True
    cnt += 1
    for i in computer_map[dd]:
        if visited[i]:
            continue
        dfs(i)



n = int(input())
node = int(input())

computer_map = [[] for _ in range(n+1)]

for _ in range(node):
    node1 , node2 = map(int,input().split())
    computer_map[node1].append(node2)
    computer_map[node2].append(node1)

visited = [0] * (n+1)
dfs(1)
print(cnt-1)
# print(computer_map)