R, C = map(int, input().split())
pasture = [list(input()) for _ in range(R)]

flag = False

for i in range(R):
    for j in range(C):
       
        # 늑대라면
        if pasture[i][j] == 'W':
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if(0<=nx<R and 0<=ny<C and pasture[nx][ny]=='S'):
                    flag = True    
                    break
        
        # 양이라면
        elif pasture[i][j] == 'S':
            continue
        
        # 빈칸이라면
        else:
            pasture[i][j] = 'D'

if flag == False:
    print(1)
    for i in pasture:
        print(''.join(i))
elif flag == True:
    print(0)