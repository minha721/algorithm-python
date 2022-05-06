def func1(str):
    return str[:-1]

def func2(str):
    rev = ''.join(reversed(str))
    return rev[:-1]

def solution(now):
    if now == S:
        return 1
    if len(now)<=len(S):
        return 0

    answer = 0
    if now[-1] == 'A':
        answer = solution(func1(now))
    if answer == 1:
        return 1
    if now[0] == 'B':
        answer = solution(func2(now))
    
    return answer

S = input()
T = input()
print(solution(T))