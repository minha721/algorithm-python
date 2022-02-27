string = input().upper()
string_set = list(set(string))
cnt = []

for i in string_set:
    cnt.append(string.count(i))

if cnt.count(max(cnt)) > 1 :
    print('?')
else:
    index = cnt.index(max(cnt))
    print(string_set[index])