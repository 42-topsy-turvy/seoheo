n = int(input())
changes = 0 #거스름돈 동전의 개수

while True:
    #가장 간단한 5원짜리로만 되는경우
    if n % 5 == 0 :
        changes += n//5
        break
    else: #2원씩 거슬러주면서 5의 배수로 만들기
        n -= 2
        changes += 1
    # 이제 거슬러 줄수가 없음
    if n < 0 :
        break

if n < 0 : 
    print(-1)
else:
    print(changes)