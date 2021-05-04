# Online Python compiler (interpreter) to run Python online.
def check_balance(expression):
    open_list = ['(', '[', '{']
    close_list = [')', ']', '}']
    stack = []
    for c in expression:
        if c in open_list:
            stack.append(c)
        elif c in close_list:
            pos = close_list.index(c)
            if len(stack) > 0 and stack[-1] == open_list[pos]:
                stack.pop()
            else:
                return False 
    return True if not stack else False


n = int(input())
for i in range(n):
    exp = input()
    print(check_balance(exp))