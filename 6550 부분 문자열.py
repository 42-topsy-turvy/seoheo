while True :
    #실행할 코드
    try :
        s, t = input().split()
    
        value = 0
        flag = 0
        #문자열을 받으면 바로 index 사용가능
        for i in range(len(t)) :
            if t[i] == s[value] :
                value += 1
            if value == len(s) :
                flag = 1
                break
        if flag == 1:
            print('Yes')
        else :
            print('No')
    #예외가 발생했을 때 처리하는 코드
    except :
        break
