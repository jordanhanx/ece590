"""
ECE 590
Project 2
Fall 2022

p2stack.py

Partner 1: Can Pei, netID: cp357
Partner 2: Xu (Jordan) Han, netID: xh123
Date: 12/4/2022
"""

"""
Stack Class
"""
class Stack:

    """
    Class attributes:
    stack    # The array for the stack.
    top      # The index of the top of the stack.
    numElems # The number of elements in the stack.
    """

    """
    __init__ function to initialize the Stack.
    Note: intially the size of the stack defaults to 3.
    Note: the stack is initally filled with None values.
    Note: since nothing is on the stack, top is -1.
    """
    def __init__(self, size=3):
        self.stack = [None for x in range(0,size)]
        self.top = -1
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.stack)) + ' ]\n'
        s += ('Top: %d' % self.top) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the stack is full.
    """
    def isFull(self):
        if (self.numElems == len(self.stack)):
            return True
        else:
            return False

    """
    isEmpty function to check if the stack is empty.
    """
    def isEmpty(self):
        if (self.numElems == 0):
            return True
        else:
            return False
        
    """
    resize function to resize the stack by doubling its size.
    """
    def resize(self):
        newstack = [None for x in range(0,2*len(self.stack))]
        for i in range(0, self.top + 1):
            newstack[i] = self.stack[i]
        self.stack = newstack
        return

    """
    push function to push a value onto the stack.
    """
    def push(self, val):
        #if stack is full, resize it
        if (self.isFull()):
            self.resize()
        
        self.stack[self.top + 1] = val
        self.numElems += 1
        self.top += 1
        return

    """
    pop function to pop the value off the top of the stack.
    """
    def pop(self):
        #if stack is empty, return none and do not change anything else
        if (self.isEmpty()):
            return None
        else:
            topval = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            self.numElems -= 1
            return topval
        
