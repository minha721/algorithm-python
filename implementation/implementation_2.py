N, M = map(int, input().split())
command = []
train = [[0]*20 for _ in range(N)]

for i in range(M):
    command.append(list(map(int, input().split())))


def command_1(numT, numS):
    if train[numT-1][numS-1] == 0:
        train[numT-1][numS-1] = 1


def command_2(numT, numS):
    if train[numT-1][numS-1] == 1:
        train[numT-1][numS-1] = 0


def command_3(numT):
    for i in range(19, 0, -1):
        train[numT-1][i] = train[numT-1][i-1]
    train[numT-1][0] = 0


def command_4(numT):
    for i in range(19):
        train[numT-1][i] = train[numT-1][i+1]
    train[numT-1][19] = 0


for i in command:
    if i[0] == 1:
        command_1(i[1], i[2])
    if i[0] == 2:
        command_2(i[1], i[2])
    if i[0] == 3:
        command_3(i[1])
    if i[0] == 4:
        command_4(i[1])

train_set = set(list(map(tuple, train)))
print(len(train_set))
