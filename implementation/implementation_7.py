N, K = map(int, input().split())

q = []
for i in range(N):
    q.append(i+1)

cnt = 0
ans = []
while q:
    cnt += 1
    if cnt % K == 0:
        ans.append(q.pop(0))
    else:
        q.append(q.pop(0))

print('<', end='')
for i in range(N - 1):
    print(ans[i], end=', ')
print(ans[-1], end = '')
print('>')