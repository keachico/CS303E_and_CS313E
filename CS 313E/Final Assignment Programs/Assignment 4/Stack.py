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

class Stack:

        #"""Define a Stack ADT with operations: Stack, isEmpty, push, pop, peek, and len."""

    def __init__(self):
            self._items = []

    def isEmpty(self):
            return not len(self._items)

    def push(self, item):
            self._items.append(item)

    def pop(self):
            return self._items.pop()

    def peek(self):
            return self._items[-1]

    def __len__(self):
            return len(self._items)

    def __str__(self):
            output = ""
            for x in self._items:
                    output = str(x) + " " + output
            return "[ " + output + "]"
