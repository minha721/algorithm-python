K = int(input())
account = []

for i in range(K):
    cost = int(input())
    if cost == 0:
        account.pop()
    else:
        account.append(cost)

print(sum(account))