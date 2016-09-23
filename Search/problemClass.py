from helper import *
from bfs import *


class Puzzle(object):
    def __init__(self, initial, inputR, inputC, goal=None):
        self.initial = initial
        self.size = len(initial)
        self.cRow = inputR
        self.cCol = inputC
        self.goal = goal
        # Generate all possible actions
        self.actions = permute([i for i in range(1, self.size + 1)])

    def getActions(self, state):
        lineIndex = self.size
        # lineIndex denote the first line contains zero. This line is going to be operated.
        for row in range(self.size):
            if lineIndex != self.size:
                break
            for col in range(self.size):
                if state[row][col] == 0:
                    lineIndex = row
                    break
        # if all squares are filled, no action can be applied.
        if lineIndex == self.size:
            return []
        else:
            tempActions = []
            currentLine = state[lineIndex]
            # unfilledIndex holds the column indexes of blank square. it can indicates the position of squares in state
            # with lineIndex.
            # every element in possibleNumber is a list of bool value
            unfilledIndex = []
            possibleNumber = []
            # make unfilledIndex
            for c in range(0, self.size):
                if currentLine[c] == 0:
                    unfilledIndex.append(c)
            # For every number unfilledIndex denotes, check all other numbers which are in same row, column or box the
            # number.
            for c in unfilledIndex:
                a = [True for i in range(self.size + 1)]
                factorR = lineIndex//self.cRow
                factorC = c//self.cCol
                for x in range(self.cRow):
                    for y in range(self.cRow):
                        a[state[x + factorR * self.cRow][y + factorC * self.cCol]] = False
                for r in range(self.size):
                    a[state[r][c]] = False
                possibleNumber.append(a)
            # for loop compare every action with currentLine, check if actions are compatible to currentLine,
            # then add it to tempActions.
            for action in self.actions:
                isFit = True
                for c in range(0, self.size):
                    if currentLine[c] == 0:
                        # 0 can't conflict with any number, it means empty.
                        continue
                    if not currentLine[c] == action[c]:
                        isFit = False
                        break
                # if the action is fit to currentLine and a legal action, add it to tempAction.
                for i in range(len(unfilledIndex)):
                    isFit = isFit and possibleNumber[i][action[unfilledIndex[i]]]
                if isFit:
                    tempActions.append(action)
            return tempActions

    def applyAction(self, state, action):
        # get lineIndex
        lineIndex = self.size
        for row in range(self.size):
            if lineIndex != self.size:
                break
            for col in range(self.size):
                if state[row][col] == 0:
                    lineIndex = row
                    break
        newState = deepcopy(state)
        newState[lineIndex] = action
        return newState

    def isGoal(self, state):
        if not state:
            return False
        # check if the whole puzzle is filled. if the puzzle is not filled, it is clear that it is not our goal state.
        lineIndex = self.size
        for row in range(self.size):
            if lineIndex != self.size:
                break
            for col in range(self.size):
                if state[row][col] == 0:
                    lineIndex = row
                    break
        if lineIndex < self.size:
            return False
        # check columns
        for col in range(self.size):
            if len(set([row[col] for row in state])) < self.size:
                return False
        # check boxes
        for box in makeBoxes(state, self.cRow, self.cCol):
            if len(set(box)) < self.size:
                return False
        return True
