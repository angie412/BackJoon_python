import sys
sys.setrecursionlimit(10**6)
bst = []

n = 0
def postorder(start, end) :
    if start > end:
        return
    
    index = start + 1
    for i in range(start+1, end+1):
        if bst[start] < bst[i]:
            index = i
            break

    postorder(start + 1, index-1)
    postorder(index, end)
    print(bst[start])



while True:
    try :
        n = int(input())
        bst.append(n)
    except :
        break
length = len(bst)
postorder(0,length-1)       