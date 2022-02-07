from bisect import bisect_left

cnt = []
T = int(input())

def count(A, B):
    cur_cnt = 0
    for i in A:
        cur_cnt += bisect_left(B, i)
    return cur_cnt        

for i in range(T):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        A.sort()
        B.sort()
        cnt.append(count(A, B))

for i in cnt:
    print(i)