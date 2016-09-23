from bfs import *
from problemClass import *
from bfs import *
import time



p1 = [[3,4,1,0],
      [0,2,0,0],
      [0,0,2,0],
      [0,1,4,3]]

p2 = [[1,5,0, 0,4,0],
      [2,4,0, 0,5,6],

      [4,0,0, 0,0,3],
      [0,0,0, 0,0,4],

      [6,3,0, 0,2,0],
      [0,2,0, 0,3,1]]

p3 = [[0,0,0, 0,4,0],
      [5,6,0, 0,0,0],

      [3,0,2, 6,5,4],
      [0,4,0, 2,0,3],

      [4,0,0, 0,6,5],
      [1,5,6, 0,0,0]]

p4 = [[0,0,0, 8,4,0, 6,5,0],
      [0,8,0, 0,0,0, 0,0,9],
      [0,0,0, 0,0,5, 2,0,1],

      [0,3,4, 0,7,0, 5,0,6],
      [0,6,0, 2,5,1, 0,3,0],
      [5,0,9, 0,6,0, 7,2,0],

      [1,0,8, 5,0,0, 0,0,0],
      [6,0,0, 0,0,0, 0,4,0],
      [0,5,2, 0,8,6, 0,0,0]]





def solver(initialPuzzle, r, c, search='bfs', printSolution=False):
    problem = Puzzle(initialPuzzle, r, c)
    result = Node([])
    if search == 'bfs':
        result = BFS(problem)
    elif search == 'dfs':
        result = DFS(problem)
    if printSolution:
        if result.getState():
            for line in result.getState():
                print(line)
        else:
            print('No Solution')
    return result.getState()

solver(p4, 3, 3, 'dfs', True)
