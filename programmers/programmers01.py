# level1 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    zero = lottos.count(0)
    match = 6-len(list(set(win_nums)-set(lottos)))
    
    answer = [rank(match+zero), rank(match)]
    return answer

def rank(match):
    if match > 1:
        return 7-match
    else:
        return 6

# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]

# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

print(solution(lottos, win_nums))