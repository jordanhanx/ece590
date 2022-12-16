"""
ECE 590
Project 2
Fall 2022

project2.py

Partner 1: Can Pei, netID: cp357
Partner 2: Xu (Jordan) Han, netID: xh123
Date: 12/4/2022
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')

    ##### Your implementation goes here. #####
    ### DFS ###
    if (alg == 'DFS'):
        todo = Stack()
    ### BFS ###
    else:
        todo = Queue()
    ### iteration ###
    # The iterative algorithm refers to <<All of Programming>> pages 479 to 480
    
    # I cannot clear the visited attribute of all Vertices in this scope, \
    # So I use a Set to store visited Vertices
    set_visited = set()
    todo.push([maze.start])
    while not todo.isEmpty():
        path = todo.pop()
        # if the last vertex of current path is exit, then return
        if maze.exit.isEqual(path[-1]):
            return [obj.rank for obj in path]
        # if the last vertex of current path is not visited, mark it
        elif path[-1] not in set_visited:
            set_visited.add(path[-1])
            # create new path towards its neighboring vertices
            for adj in path[-1].neigh:
                if adj.visited != True:
                    new_path = [obj for obj in path]
                    new_path.append(adj)
                    todo.push(new_path) # push new path into todo
    return []
    ##### Your implementation goes here. #####

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)
