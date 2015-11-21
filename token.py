

class Buffer(object):

    def __init__(self, data):
        self.data = data
        self.offset = 0

    def peek(self):
        if self.offset >= len(self.data):
            return
        return self.data[self.offset]

    def advance(self):
        self.offset += 1


class Token(object):

    def consume(self, buffer):
        pass


class IntToken(Token):

    def consume(self, buffer):
        accum = ""
        while True:
            ch = buffer.peek()
            if ch is None:
                break
            if ch in "1234567890.":
                accum += ch
                buffer.advance()
            else:
                break

        if accum != "":
            return ("float", float(accum))
        else:
            return None


class OperatorToken(Token):

    def consume(self, buffer):
        ch = buffer.peek()
        if ch is not None and ch in "+-*/()^%":
            buffer.advance()
            return ("oper", ch)
        return None
