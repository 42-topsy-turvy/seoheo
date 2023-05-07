N = int(input())
dasom = int(input()) #다솜이 지정
candidate = []
bribe = 0

for _ in range(N - 1):
    candidate.append(int(input()))
candidate.sort(reverse=True) #내림차순 정렬
if N == 1 :
       print(0)
else :
    while candidate[0] >= dasom :
        bribe += 1
        candidate[0] -= 1
        dasom += 1
        candidate.sort(reverse=True)
    print(bribe)