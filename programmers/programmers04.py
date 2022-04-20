# level2 기능 개발

from collections import deque
from math import ceil

def solution(progresses, speeds):
    time = deque()
    fin = deque()
    answer = deque()

    for i in range(len(progresses)):
        # 일(day) 단위로 봐야 해서 남은 시간이 소숫점이면 올림
        time.append(ceil((100-progresses[i])/speeds[i]))

    while time:
        cur = time.popleft()
        fin.append(cur)

        while(True):
            if time:
                next = time.popleft()
                
                if cur < next :
                    time.appendleft(next)
                    answer.append(len(fin))
                    fin.clear()
                    break
                elif cur >= next :
                    fin.append(next)

            else:
                answer.append(len(fin))
                break

    return list(answer)

# progresses = [95, 95, 95, 95]
# speeds = [4, 3, 2, 1]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))