"""
ECE 590
Project 2
Fall 2022

p2queue.py

Partner 1: Can Pei, netID: cp357
Partner 2: Xu (Jordan) Han, netID: xh123
Date: 12/4/2022
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        if (self.numElems == len(self.queue)):
            return True
        else:
            return False

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        if (self.numElems == 0):
            return True
        else:
            return False

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        newqueue = [None for x in range(0,2*len(self.queue))]
        #build queue in a circle, so rear may be smaller than front, need to divide into 2 parts
        #1st: from front to end of array
        for i in range(self.front, len(self.queue)):
            newqueue[i-self.front] = self.queue[i]
        
        #2nd: from begin of array to rear
        for j in range(0, self.rear):
            newqueue[j + len(self.queue) - self.front] = self.queue[j]
            
        #reset front and rear
        self.front = 0
        self.rear = len(self.queue)
        self.queue = newqueue
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        #if queue is full, resize
        if (self.isFull()):
            self.resize()
        
        #if rear goes beyond the end of array, turn back to the begin of array
        self.queue[self.rear] = val
        self.rear = (self.rear + 1) % len(self.queue)
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        #if queue is empty, return none and do not change anything else
        if (self.isEmpty()):
            return None
        else:
            topval = self.queue[self.front]
            self.queue[self.front] = None
            #if front goes beyond the end of array, turn back to the begin of array
            self.front = (self.front + 1) % len(self.queue)
            self.numElems -= 1
            return topval