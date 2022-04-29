def solution(s):
    s_lower = s.lower()
    s_cnt = [0]*(26)

    for i in s_lower :
        # a는 index 0, b는 index 1, ... 에 문자 카운트 저장
        s_cnt[ord(i)-97] += 1

    max_index = [i for i, value in enumerate(s_cnt) if value == max(s_cnt)]

    max_alpha = []
    for i in max_index:
        max_alpha.append(chr(i+97))

    answer = ''.join(max_alpha)
    return answer