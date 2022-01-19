from itertools import product

product_tmp = []

n, num_k = map(int, input().split())
k = list(map(str, input().split()))

for i in range(1, len(str(n))+1):
    product_tmp.append(list(map(''.join, product(k, repeat=i))))

lproduct = sorted(list(map(int, sum(product_tmp, []))))

for i in range(len(lproduct), 0, -1):
    if int(lproduct[i-1]) <= n:
        print(int(lproduct[i-1]))
        break
