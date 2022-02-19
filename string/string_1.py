n = int(input())
text = input()
second = int(input())

# text 한글자씩 넣은 큐
char = []
# 출력할 거
str = []

for i in text :
    if i == ' ':
        char.append('_')
    else:
        char.append(i)

turn = n + len(text) - 1
index = second % turn

# 0초일 때 전부 빈칸으로 설정
for i in range(n):
    str.append('_')

for i in range(1, turn+1):
    del str[0]
    
    if i <= len(text) :
        str.append(char[i-1])
    else :
        str.append('_')

    if i == index:
        print(''.join(str))