import string
def infixToPostfix(infixexpr):
    # First set up a dictionary mapping symbols to
    # precedence.
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    # Split the input into tokens.
    tokenList = infixexpr.split()
    # We’ll need a stack and an output stream.
    opStack = Stack()
    outputList = []
    for token in tokenList:
        # Is token a number?
        if token.isdigit():
            outputList.append(token)
        elif token == ’(’:
            opStack.push(token)
        elif token == ’)’:
            topToken = opStack.pop()
            while topToken != ’(’:
                outputList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                outputList.append(opStack.pop())
                                
            opStack.push(token)
                                
    while not opStack.isEmpty():
        outputList.append(opStack.pop())
    return ’ ’.join(outputList)
