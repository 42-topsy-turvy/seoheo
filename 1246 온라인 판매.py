N, M = map(int, input().split())
customers = [int(input()) for i in range(M)]
revenue = 0 #초기 수익
price = 0 #초기 가격

customers.sort() #구매희망자 리스트 오름차순 정렬
for i in customers:
    # 판매 가능한 계란수 > 구매희망 계란수 이면 continue
    # M - customers.index(i) 는 판매 가능한 계란수
    if (M - customers.index(i)) > N :
        continue
    # sales 는 가격 * 판매가능 계란(매출이란 뜻으로 사용했는데 엄밀히는 아님)
    sales = i * (M - customers.index(i))
    if sales > revenue :
        revenue = sales
        price = i
print(price, revenue)