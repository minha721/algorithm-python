T = int(input())

for i in range(T) :
    total = 0
    score = 0
    before = 'X'
    case = list(input())

    for i in range(len(case)):
        now = case.pop(0)
        if now == 'O':
            score += 1
            total += score
        elif now == 'X' :
            score = 0
        before = now
    print(total)