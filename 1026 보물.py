N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
A.sort() # A만 정렬가능

for i in range(N): #A가 가장 작을때 제일 큰 B를 뽑아 낸다(pop)
    x = A[i]
    y = B.pop(B.index(max(B)))

    ans += x * y

print(ans)