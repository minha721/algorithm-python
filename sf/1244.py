# 스위치 정보 입력
num_sw = int(input())
switch = list(map(int, input().split()))
switch.insert(0, 0)

# 학생 정보 입력
num_st = int(input())
student = []
for i in range(num_st):
    student.append(list(map(int, input().split())))

for i in student:
    # 남학생이면 -> 완료
    if i[0] == 1:
        for j in range(1, num_sw + 1):
            if j % i[1] == 0:
                if switch[j] == 1:
                    switch[j] = 0
                elif switch[j] == 0:
                    switch[j] = 1
    # 여학생이면
    elif i[0] == 2:
        # 스위치 대칭 구간 찾기
        start = i[1]
        index = 1
        while True:
            left = start - index
            right = start + index
            if left < 1 or right > num_sw:
                break
            elif switch[left] != switch[right]:
                break
            elif switch[left] == switch[right]:
                index += 1

        # 스위치 변경
        for j in range(left+1, right):
            if switch[j] == 1:
                switch[j] = 0
            elif switch[j] == 0:
                switch[j] = 1

del switch[0]

for i in range(len(switch)):
    if (i+1) // 20 > 0 and (i+1) % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end=' ')