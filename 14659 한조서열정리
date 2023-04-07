N = int(input())
heights = list(map(int,input().split()))

maxheight = 0
count = 0
killlog = []
for i in heights :
    if i > maxheight :
        maxheight = i
        count = 0
    else :
        count += 1
    killlog.append(count)

print(max(killlog))