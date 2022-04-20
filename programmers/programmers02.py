# level1 없는 숫자 더하기

def solution(numbers):
    nums = [i for i in range(10)]
    answer = 0
    for i in list(set(nums)-set(numbers)):
        answer += i
    return answer

# numbers = [1,2,3,4,6,7,8,0]
numbers = [5,8,4,0,6,7,9]
print(solution(numbers))