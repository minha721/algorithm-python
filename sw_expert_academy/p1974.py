graph = []
for i in range(9):
    graph.append(list(map(int, input().split())))

def chk_num(l):
    slist = sorted(l)
    if slist == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    else:
        return False

def set_list(x, y):
    mlist = []
    for i in range(3):
        for j in range(3):
            mlist.append(graph[x + i][y + j])
    return mlist

res = True
for i in graph:
    res *= chk_num(i)

if res == True:
    for i in range(9):
        nlist = []
        for j in range(9):
            nlist.append(graph[j][i])
        res *= chk_num(nlist)

if res == True:
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            nlist = set_list(i, j)
            res *= chk_num(nlist)

print(res)