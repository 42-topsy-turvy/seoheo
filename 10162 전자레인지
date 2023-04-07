T = int(input())

buttons = [300, 60, 10]

press = []
for i in buttons :
    press.append(T // i)
    T = T % i
    if (T > 0 and T < 10) :
        T = -1
        print("-1")
        break

if(T != -1) :
    print(*press)