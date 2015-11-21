from token import *

def tokenize(string):
    buffer = Buffer(string)
    tk_int = IntToken()
    tk_oper = OperatorToken()
    tokens = []

    while buffer.peek():
        token = None

        for tk in (tk_int, tk_oper):
            token = tk.consume(buffer)
            if token is not None:
                tokens.append(token)
                break

        if token is None:
            # in case of unknow operator
            raise ValueError("Syntax Error(unknow operator).")

    return tokens