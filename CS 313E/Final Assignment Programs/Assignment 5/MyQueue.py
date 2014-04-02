#  Files: MyQueue.py
#
#  Description: Create a Queue class: first in first out implementation 
#
#  Student's Name: Nadeem Abha, Kevin Achico
#
#  Student's UT EID: na4333, ka6893
#
#  Course Name: CS 313E 
#
#  Date Created: 10/11/12
#
#  Date Last Modified: 10/15/12


class MyQueue:
    
    def __init__(self):
        self.items = []
        
    def __str__(self):
        print (self.items)
        
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return not len(self.items)
    
    def peek(self):
        return self.items[-1]
    
