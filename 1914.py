# move(n, start, end, mid)
# n-1 -> B , move(n-1, start, mid, end) , n-> C 
# 1 : 1, 2 : 3, 3 : 7, 4 : 15 --> 2^n - 1

def move(start, mid, end, cnt):
    if cnt == 1:
        print(start, end)
        return
    move(start, end, mid, cnt-1)
    print(start, end)

    move(mid, start, end, cnt-1)


N = int(input())

print(2**N -1)
if N<=20:
    move(1,2,3,N)
