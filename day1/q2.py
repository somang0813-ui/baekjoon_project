import sys
sys.setrecursionlimit(10000)
def solution(maps):

    answer = []
    ##가로 길이
    map_w = len(maps[0])
    ##세로 길이
    map_h = len(maps)
    is_Counted = [[0] * map_w for i in range(map_h)]

    ## 섬의 식량을 세는 함수
    def countMaxDay(maps,a,b):
        MaxDay = int(maps[a][b])
        is_Counted[a][b] = 1
        
        ## <
        if b - 1 >= 0 and is_Counted[a][b - 1] == 0 and maps[a][b - 1] != "X":
            MaxDay += countMaxDay(maps,a,b - 1)
        ## >
        if b + 1 < map_w and is_Counted[a][b + 1] == 0 and maps[a][b + 1] != "X":
            MaxDay += countMaxDay(maps,a,b + 1)
        ## v
        if a + 1 < map_h and is_Counted[a + 1][b] == 0 and maps[a + 1][b] != "X":
            MaxDay += countMaxDay(maps,a + 1,b)
        ## ^
        if a - 1 >= 0 and is_Counted[a - 1][b] == 0 and maps[a - 1][b] != "X":
            MaxDay += countMaxDay(maps,a - 1,b)
        return MaxDay
    
    ##섬 전체를 순회
    for i in range(map_h):
        for j in range(map_w):
            if maps[i][j] != "X" and is_Counted[i][j] == 0 :
                answer.append(countMaxDay(maps=maps,a=i,b=j))
    ## 섬이 없는 경우
    if len(answer) == 0:
        answer.append(-1)

    ## 배열 정렬
    answer.sort()
    return answer