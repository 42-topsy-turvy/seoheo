money = 1000 - int(input())
changes = [500, 100, 50, 10, 5, 1]
count = 0
for i in changes :
    count += money//i
    money %= i
print(count)