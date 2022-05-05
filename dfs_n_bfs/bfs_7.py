def solution(numbers, target):
    answer = 0
    sum = [0]

    for i in numbers:
        calc = []
        for j in sum:
            calc.append(j+i)
            calc.append(j-i)
        sum = calc

    for i in sum:
        if i == target:
            answer += 1
    return answer