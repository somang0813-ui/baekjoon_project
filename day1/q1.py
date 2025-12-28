T = int(input())
result = []

for _ in range(T):
    a, b = map(int,input().split())
    a = a % 10
    
    ## a 는 1의 자리수
    match a:
        ##패턴 길이 = 1
        case 0:
            result.append(10)
        case 1:
            result.append(1)
        case 5: 
            result.append(5)
        case 6:
            result.append(6)
        ## 패턴 길이 = 2 (a = 4,9)
        case 4 | 9:
            if(b % 2 == 0):
                result.append((a ** 2) % 10)
            else:
                result.append(a ** ((b % 2)) % 10)
        ## 패턴 길이 = 4 (a = 2,3,7,8)
        case 2 | 3 | 7 | 8:
            if(b % 4 == 0):
                result.append((a ** 4) % 10)
            else:
                result.append(a ** ((b % 4)) % 10)

for i in result:
    print(i)