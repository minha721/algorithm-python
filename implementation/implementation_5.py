remain = []

for i in range(10):
    remain.append(int(input())%42)

set_remain = list(set(remain))

print(len(set_remain))