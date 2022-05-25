info = input()

cards = []
S = []
D = []
H = []
C = []

for i in range(0, len(info)-2, 3):
    cards.append(info[i:i+3])

for i in cards:
    if i[0] == "S":
        S.append(i)
    elif i[0] == "D":
        D.append(i)
    elif i[0] == "H":
        H.append(i)
    elif i[0] == "C":
        C.append(i)

if len(S) == len(list(set(S))) and len(D) == len(list(set(D))) and len(H) == len(list(set(H))) and len(C) == len(list(set(C))):
    print("{} {} {} {}".format(13-len(S), 13-len(D), 13-len(H), 13-len(C)))
else:
    print("ERROR")