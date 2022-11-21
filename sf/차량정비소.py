for tc in range(int(input())):
    N, M, K, A, B = map(int, input().split())
    # 접수 창구 처리 속도
    a_list = list(map(int, input().split()))
    # 정비 창구 처리 속도
    b_list = list(map(int, input().split()))
    # 접수 창구에 고객이 도착한 시각.
    t_list = list(map(int, input().split()))

    # 길이 N만큼 [고객 번호, 작업 완료까지 남은 시간]
    receptionDesk = [[0, 0] for _ in range(N)]
    # 길이 M만큼 [고객 번호, 작업 완료까지 남은 시간]
    repairDesk = [[0, 0] for _ in range(M)]

    reception_waiting = []
    repair_waiting = []

    # 길이 K만큼 [접수 창구, 정비 창구]
    history = [[0, 0] for _ in range(K)]
    time = 0

    while True:
        # 접수 창구 하나씩 탐색
        for i in range(N):
            # 사람이 존재하면 작업 완료까지 남은 시간 줄이기
            if receptionDesk[i][1] > 0:
                receptionDesk[i][1] -= 1

            # 사람이 존재하고 작업 완료까지 남은 시간이 0이면 정비 창구로 보냄
            if receptionDesk[i][1] == 0 and receptionDesk[i][0] > 0:
                repair_waiting.append(receptionDesk[i][0])
                history[receptionDesk[i][0] - 1][0] = i + 1
                receptionDesk[i] = [0, 0]

            # 접수 창구가 비었으면 고객 채워줌. 작업 남은 시간 초기화
            if receptionDesk[i][0] == 0:
                if reception_waiting:
                    receptionDesk[i] = [reception_waiting.pop(0), a_list[i]]

                # 정비 창구 하나씩 탐색
        for i in range(M):
            # 사람이 존재하면 작업 완료까지 남은 시간 줄이기
            if repairDesk[i][1] > 0:
                repairDesk[i][1] -= 1

            # 사람이 존재하고 작업 완료까지 남은 시간이 0이면 보냄
            if repairDesk[i][0] > 0 and repairDesk[i][1] == 0:
                history[repairDesk[i][0] - 1][1] = i + 1
                repairDesk[i] = [0, 0]

            # 정비 창구가 비었으면 고객 채워줌. 작업 남은 시간 초기화.
            if repairDesk[i][0] == 0:
                if repair_waiting:
                    repairDesk[i] = [repair_waiting.pop(0), b_list[i]]

        # 현재 시각에 접수 창구에 도착한 고객이 있다면 웨이팅에 저장
        for i in range(K):
            if t_list[i] == time:
                reception_waiting.append(i + 1)

        time += 1

        # while문 탈출 조건 : 모든 사람 업무 끝냈을 때
        count = 0
        for temp in history:
            if temp[0] > 0 and temp[1] > 0:
                count += 1
        if count == K:
            break

        # 지갑 잃어버린 사람이랑 같은 창구 이용한 고객 번호 더하기
    result = 0
    for idx, temp in enumerate(history):
        if temp == [A, B]:
            result += (idx + 1)

    if result:
        print("#{} {}".format(tc + 1, result))
    else:
        print("#{} -1".format(tc + 1))