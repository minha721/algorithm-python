N = int(input())
words = []
for i in range(N):
    words.append(input())
 
set_words = list(set(words))
sort_words = []

for i in set_words:
    sort_words.append((len(i), i))
 
sort_words.sort()
 
for len, word in sort_words:
    print(word)