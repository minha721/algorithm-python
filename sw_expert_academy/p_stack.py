size = int(input())
stack = []

while True:
    # 스택이 가득 차면
    if len(stack) == size:
        print("stack is full!")
        while True:
            # 스택이 비어지면
            if len(stack) == 0:
                print("stack is empty!")
                break
            else:
                print(stack.pop())
        break
    else:
        stack.append(int(input()))