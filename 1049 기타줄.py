N, M = map(int, input().split())

minpackage = 1001 #입력 가능한 최대가격보다 큰 값으로 초기화
minsingle = 1001 
for brand in range(M):
    package, single = map(int, input().split())
    minpackage = min(minpackage, package) #입력시 마다 최소값으로 초기화
    minsingle = min(minsingle, single)

cost = 0
#패키지 가격이 낱개 * 6 보다 가격이 크면 낱개로 모두 구매
if minpackage > minsingle*6:
    cost += N * minsingle
else:
		#패키지가 더 저렴할 때
		#망가진 기타줄의 수를 N으로 나눈만큼 패키지로 구매
    cost += (N//6) * minpackage
    
		#남은 낱개의 가격 * 6이 패키지보다 크면 패키지로 구매
    if (N % 6) * minsingle > minpackage:
        cost += minpackage
    else:
		#아닐시 낱개로 구매
        cost +=(N%6)*minsingle

print(cost)