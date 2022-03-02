N = int(input())
pattern = input()

file = []
for i in range(N):
    file.append(input())

pattern = pattern.split('*')

for i in file:
    if len(i) >= len(pattern[0]) + len(pattern[1]) :
        start = i[0:len(pattern[0])]
        end = i[-len(pattern[1]):]
        if pattern[0]==start and pattern[1]==end:
            print("DA")
        else:
            print("NE")
    else:
        print("NE")