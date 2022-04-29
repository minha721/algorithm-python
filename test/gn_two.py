def solution(N):
    str_N = str(N)
    list_N = [i for i in str_N]

    asc_num = int(''.join(sorted(list_N)))
    desc_num = int(''.join(sorted(list_N, reverse=True)))

    answer = asc_num + desc_num
    return answer