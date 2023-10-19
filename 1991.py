# 첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 
# 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 
# 오른쪽 자식 노드가 주어진다. 
# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 
# 자식 노드가 없는 경우에는 .으로 표현한다.

# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 
# 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.

import sys

input = sys.stdin.readline
n = int(input())

bst = {}
for _ in range(n):
    root, left, right = input().split()
    bst[root] = [left, right]
# 트리 노드 받아옴

def preorder(root):
    if root != '.' :
        print(root, end = '')
        preorder(bst[root][0])
        preorder(bst[root][1])

def inorder(root):
    if root !='.':
        inorder(bst[root][0])
        print(root, end='')
        inorder(bst[root][1])

def postorder(root):
    if root != '.':
        postorder(bst[root][0])
        postorder(bst[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')


        