def solution(numbers):
    majority = len(numbers)//2
    set_nums = list(set(numbers))

    for i in set_nums:
        cnt = numbers.count(i)
        if cnt > majority:
            answer = i
            break
        answer = -1

    return answer