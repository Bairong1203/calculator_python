from collections import deque

def query_priority(oper):
    priority = ["#", "+-", "*/%", "^", ]
    for str in priority:
        if oper in str:
            return priority.index(str)
    return -1


def parse(tokens):
    if tokens[0][0] == 'oper' and tokens[0][1] != '(':
        # in case of bad expression
        raise ValueError("Syntax Error(bad expression).")

    oper_stack = ['#']
    rpn = []

    for token in tokens:
        if token[0] == 'float':
            rpn.append(token[1])

        elif token[0] == 'oper':
            if token[1] == '(':
                oper_stack.append(token[1])

            elif token[1] == ')':
                while oper_stack[-1] != '#':
                    oper = oper_stack.pop()
                    if oper == '(':
                        break
                    rpn.append(oper)
                if oper != '(':
                    raise ValueError("Syntax Error(bad expression).")

            elif query_priority(token[1]) > query_priority(oper_stack[-1]):
                oper_stack.append(token[1])

            else:
                while query_priority(token[1]) <= query_priority(oper_stack[-1]):
                    rpn.append(oper_stack.pop())

                oper_stack.append(token[1])

    while oper_stack[-1] != '#':
        rpn.append(oper_stack.pop())

    return rpn


def calculate(rpn):
    queue = deque(rpn)
    queue.append("#")
    stack = []
    elem = queue.popleft()
    while elem != '#':
        if type(elem) == float:
            stack.append(elem)
        else:
            try:
                rightval = stack.pop()
                leftval = stack.pop()
            except:
                raise ValueError("Syntax Error(bad expression)")
            if type(leftval) != float or type(rightval) != float:
                raise ValueError("Syntax Error(bad expression)")
            if elem == '+':
                stack.append(leftval + rightval)
            elif elem == '-':
                stack.append(leftval - rightval)
            elif elem == '*':
                stack.append(leftval * rightval)
            elif elem == '/':
                stack.append(leftval / rightval)
            elif elem == '%':
                stack.append(leftval % rightval)
            elif elem == '^':
                stack.append(leftval**rightval)
        elem = queue.popleft()

    return stack[-1]
