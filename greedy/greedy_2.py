price = []
total_price = 0

n = int(input())

for i in range(n):
    price.append(int(input()))

price.sort()

if n % 3 == 1:
    total_price += price[0]
    del price[0]
elif n % 3 == 2:
    total_price += (price[0]+price[1])
    del price[0:2]

for i in range(len(price)):
    if i % 3 == 1 or i % 3 == 2:
        total_price += price[i]

print(total_price)
