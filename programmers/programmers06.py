# level2 예상 대진표

def solution(n,a,b):
    answer = 0

    while True:
        if a == b:
            break
        else:
            a = (a//2) + (a%2)
            b = (b//2) + (b%2)
            answer += 1

    return answer

# print(solution(8, 4, 7))