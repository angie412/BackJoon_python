# 괄호의 값

import sys

n = int(sys.stdin.readline().strip())
# strip 은 개행 제거 

for _ in range(n):
    input_string = sys.stdin.readline().strip()
    stack = []
    flag = 0

    for char in input_string :
        
        if char == '(':
            stack.append(char)
        
        elif char == ')':

            if not stack :
                flag = 1
                break
                
            stack.pop()
    
    if not flag and not stack :

    # flag가 0 이고 stack 이 비어있을떄 
        print('YES')
    else :
        print('NO')
