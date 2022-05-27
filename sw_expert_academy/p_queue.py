from collections import deque

size = int(input())
q = deque()

while True:
    # 큐가 가득 차면
    if len(q) == size:
        print("queue is full!")
        while True:
            # 큐가 비어지면
            if len(q) == 0:
                print("queue is empty!")
                break
            else:
                print(q.popleft())
        break
    else:
        q.append(int(input()))