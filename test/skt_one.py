# 백준 1106과 매우 유사

def solution(money, costs):
    INF = 1e9
    units = [1, 5, 10, 50, 100, 500]
    data = []

    min_cost = [INF] * (money+1)
    min_cost[0] = 0

    for i in range(len(costs)):
        data.append([costs[i], units[i]])

    data_sort = sorted(data, key = lambda x:x[0])

    for cost, unit in data_sort:
        for i in range(unit, money+1):
            min_cost[i] = min(min_cost[i-unit] + cost, min_cost[i])

    answer = min_cost[money]
    return answer