# Files: Stack.py, Calculator.py
# 
# Description: Emulates a calculator using the stack class. 
#
# Student's Name(s): Nadeem Abha, Kevin Achico
#
# Student's UT EID: na4333, ka6893
#
# Course Name: CS 313E 
#
# Date Created: October 7, 2012
#
# Date Last Modified: October 8, 2012


from Stack import *

import string


def main():

    
    user_input = input("Enter an infix expression: ") 
    while user_input != "stop": #check whether user wants to stop
        while user_input == "postfix": #if user enters "postfix", change to postfix
            print ("")
            postfixexpr = input("Input a postfix expression: ") #prompts user again

            if postfixexpr != "infix":
                try:
                    print ("The answer is: ", postEval(postfixexpr))
                except IndexError: #returns error message for ill formed expressions
                    print ("Ill-formed expression")

                except KeyError: #returns error message for invalid characters
                    print ("Ill-formed expression, bad token")

                except ZeroDivisionError: #case when attempting to divide by zero
                    print("Division by Zero is Impossible!!!!")
                    
            else: #case in which user wishes to switch back to infix expression
                print ("")
                user_input = input("Enter an infix expression: ")
       
        try:
            print ("The answer is: ", postEval(infixToPostfix(user_input)))
        except IndexError:
            print ("Ill-formed expression")

        except KeyError:
            print ("Ill-formed expression, bad token")
            
        except ZeroDivisionError:
                print("Division by Zero is Impossible!!!!")
        
        print ("")
        user_input = input("Enter an infix expression: ")
    
                  
def infixToPostfix(infixexpr):
    # First set up a dictionary mapping symbols to
    # precedence.
    prec = {}
    prec["*"]= 3
    prec["/"]= 3
    prec["+"]= 2
    prec["-"]= 2
    prec["("]= 1
    # Split the input into tokens.
    tokenList = infixexpr.split()
    # We’ll need a stack and an output stream.
    opStack = Stack()
    outputList = []
    for token in tokenList:
        # Is token a number?
        if token.isdigit():
            outputList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                outputList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                  (prec[opStack.peek()] >= prec[token]):
                outputList.append(opStack.pop())

            opStack.push(token)
                                
    while not opStack.isEmpty():
        outputList.append(opStack.pop())
    #print(" ".join(outputList))
    return " ".join(outputList)
    



def postEval(postfixexpr):
    """Given a postfix expression, evaluate it"""
    #symbolString = input("Input a postfix expression: ")
    #tokens = symbolString.split()
    tokens = postfixexpr.split()
    stack = Stack()
    #try:
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
    
    #except IndexError:
        #print ("Ill-formed expression")
            

def applyOp(token, arg1, arg2):
    
    if token == "+": #if token is "+", apply plus operator
        return (arg2 + arg1)

    elif token == "-": #if token is "-", apply subtract operator
        return (arg2 - arg1)

    elif token == "*": #if token is "*", apply multiplication operator
        return (arg2 * arg1)

    else: #else, apply division operator
        return (arg2 / arg1)

main()
