A, B, C, M = list(map(int,input().split()))

work = 0
fatigue = 0

for i in range(24) :
    if fatigue + A <= M :
        fatigue += A
        work += B
    else :
        if fatigue - C >= 0:
            fatigue -= C
        else :
            fatigue = 0

print(work)