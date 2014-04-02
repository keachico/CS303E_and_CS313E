from Stack import *


def main():
    postEval0()


def postEval0():
    """Given a postfix expression, evaluate it"""
    
    symbolString = input("Input a postfix expression: ")
    tokens = symbolString.split()
    stack = Stack()
    
    for token in tokens:
        # Is the token an integer?
        if token.isdigit():
            stack.push(int(token))
        # otherwise, it must be an operator
        else:
            arg1 = stack.pop()
            arg2 = stack.pop()
            # You’ll have to write the applyOp function
            val = applyOp(token, arg1, arg2)
            stack.push(val)
    return stack.pop()



main()
