sum = []

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

if n % 2 == 0:
    for i in range(n//2):
        sum.append(arr[i]+arr[n-i-1])
elif n % 2 == 1:
    sum.append(arr[n-1])
    for i in range(n//2):
        sum.append(arr[i]+arr[n-i-2])

print(max(sum))
