def solution(n, text, second) :
    text = text.replace(' ', '_')

    turn = n + len(text) - 1
    index = second % turn
    q = ['_']*n

    for i in range(1, turn+1):
        q.pop(0)

        if(i <= len(text)) :
            q.append(text[i-1])
        else :
            q.append('_')
        
        if(i == index) :
            answer = ''.join(q)
            return answer

    return answer

print(solution(5, "abcd ef", 9))