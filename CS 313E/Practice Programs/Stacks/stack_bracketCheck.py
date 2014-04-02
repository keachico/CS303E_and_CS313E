from Stack import *

def main():
    user_input = input("Please enter in an equation with delimiters: ")
    
    print (user_input)
    
##    for c in user_input:
##        if c == ("(" or "[" or "{"):
##            print ("huzzah!")
            
    bracketChecker(user_input) 

def bracketChecker(user_input):
    s = Stack()
    for c in user_input:
        if c == ("(" or "[" or "{"):
            s.push(c)
        elif c == (")" or "]" or "}"):
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                if not matches(top, c):
                    return False
        else:
            pass
    return True


def matches(top,c):
    if top == ")":
        return c == "("
    elif top == "]":
        return c == "["
    elif top == "}":
        return c == "{"

main()
    


