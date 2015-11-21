import tokenize
import process

if __name__ == '__main__':
    while True:
        input_str = input()
        if input_str in ["exit", "exit()", "quit", "quit()"]:
            break
        tokens = tokenize.tokenize(input_str)
        rpn = process.parse(tokens)
        print(">>", process.calculate(rpn))
