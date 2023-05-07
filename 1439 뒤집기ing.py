S = input()
count = 0
start_point = '?'

for i in S :
    if i != start_point :
        start_point = i
        count += 1

print(count//2)