A, B = map(int,input().split())
N = int(input())
bookmarks = []
for bookmark in range(N-1) :
    bookmarks.append = int(input())
min = abs(bookmark[0] - B)
while N > 0 :
    press = abs(bookmark[N] - B)
    if min > press :
        min = press
    N -= 1
print(min)
