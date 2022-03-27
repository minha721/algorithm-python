import sys
from collections import deque

def AC(arr):
    direction = True

    for j in p:
        if j == 'R':
            direction = not direction
        elif j == 'D':
            if len(arr) == 0:
                return 'error'
            else:
                if direction == True:
                    arr.popleft()
                elif direction == False:
                    arr.pop()
        
    if direction == False:
        arr.reverse()
    
    return arr

T = int(input())

for i in range(T):
    p = input()
    n = int(input())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    if n == 0:
        arr = deque()

    ans = AC(arr)
    if ans == 'error':
        print('error')
    else:
        print('[', end='')
        for i in range(len(ans)):
            if i == len(ans)-1:
                print(ans[i], end='')
            else:
                print(ans[i], end=',')
        print(']')