def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

def find_max_len(arr):
    cur_max = 0
    for start in range(100):
        for end in range(start + 1, 100):
            s = arr[start:end+1]
            if is_palindrome(s) == True:
                cur_max = max(cur_max, len(s))

    return cur_max

graph = []
for i in range(100):
    row = input()
    graph.append(list(row))

col_graph = list(map(list, zip(*graph)))

max_row = 0
max_col = 0

for i in range(100):
    cur_max_row = find_max_len(graph[i])
    max_row = max(max_row, cur_max_row)
    cur_max_col = find_max_len(col_graph[i])
    max_col = max(max_col, cur_max_col)

print(max(max_row, max_col))