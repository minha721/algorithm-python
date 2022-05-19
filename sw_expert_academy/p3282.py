# N : 물건의 개수, C : 최대 용량
N, C = map(int, input().split())
graph = [[0,0]] # 물건이 아무것도 포함되지 않은 초기 상태 설정

for i in range(N): 
    # 물건 배열에 각 물건의 무게와 가치 추가
    graph.append(list(map(int, input().split())))

# 행 : 물건의 개수+1, 열 : 무게+1인 표를 0으로 초기화
dp = [ [0]*(C+1) for _ in range(N+1) ]
 
for item in range(1, N+1): # 행
    for wi in range(1, C+1): # 열
        
        weight = graph[item][0] # 현재 물건의 가치
        value = graph[item][1] # 현재 물건의 무게
 
        if (wi < weight): # 현재 물건이 배낭의 임시 최대 용량보다 클 때
            # 물건을 넣지 않는다. 최대 가치는 이전 물건까지 고려했을 때의 최대 가치
            dp[item][wi] = dp[item-1][wi] 
        else: 
            # 더 나은 경우를 찾는다. 
            # S1. 현재 물건을 넣지 않는다. 최대 가치는 이전 물건까지 고려했을 때의 최대 가치
            # S2. 현재 물건을 넣는다. 최대 가치는 이전 물건까지 고려하고, 임시 최대 용량이 현재 무게-물건의 무게 일때의 최대 가치에 물건의 가치를 더한 값
            dp[item][wi] = max(dp[item-1][wi], dp[item-1][wi-weight] + value)
 
print(dp[N][C])