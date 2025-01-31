'''
Hello! Robot coming online.
Command the robot with:
  L - turn left
  R - turn right
  M - move forward
  ? - this message
  Q - quit
> M
Robot at (0, 1) facing North  
> L
Robot at (0, 1) facing West
> M
Robot at (-1, 1) facing West
> M
Robot at (-2, 1) facing West
> R
Robot at (-2, 1) facing North
> R
Robot at (-2, 1) facing East
> M
Robot at (-1, 1) facing East
> ?
Command the robot with:
  L - turn left
  R - turn right
  M - move forward
  ? - this message
  Q - quit
> Q
Robot shutting down.

 (W - / E + ,  N + / S - )

        N
        | 
   W --   -- E
        |
        S

'''

from enum import IntEnum
class Direction(IntEnum):
    NORTH = 1   #(0, 1)
    EAST = 2
    SOUTH = 3
    WEST = 4 

dirToStep = {
    Direction.NORTH: (0, 1), 
    Direction.EAST:  (1, 0), 
    Direction.SOUTH: (0, -1), 
    Direction.WEST:  (-1, 0) 
}

class Robot:
    def __init__(self, direction = Direction.NORTH, location = [0, 0]):
        self.direction = direction
        self.location = location 

    def rotate(self, direction):
        if direction == 'L':
            self.direction -= 1
            if self.direction == 0:
                self.direction = Direction.WEST
        else: #R
            self.direction += 1
            if self.direction == 5:
                self.direction = Direction.NORTH
        self.direction = Direction(self.direction)
        #self.print()
        return (self.direction, self.location)  # (<Direction.NORTH: 1>, [0, 1])

    def move(self):
        step = dirToStep[self.direction]
        self.location[0] += step[0]
        self.location[1] += step[1]
        #self.print()
        return (self.direction, self.location)

    def print(self):
        print("Dir:", self.direction, "Location:", self.location)     

# robot = Robot()
# res = robot.move()
# print(res)

def showHelp():
    print(    '''
    L - turn left
    R - turn right
    M - move forward
    ? - this message
    Q - quit
    ''')
    
def startProgram():
    robot = Robot()
    while True:
        cmd = input("Please input your command: ")
        if cmd in ('L', 'R'):
            robot.rotate(cmd)
        elif cmd == 'M':
            robot.move()
        elif cmd == '?':
            showHelp()
        elif cmd == 'Q':
            print("End the program")
            break
        else:
            print("Error code")

# startProgram()

import unittest
class Test(unittest.TestCase):
    # def testMove(self):  
    #     robot = Robot()
    #     res = robot.move()
    #     self.assertEquals(res, (Direction.NORTH, [0, 1]))
    # def testRotate(self):
    #     robot = Robot()
    #     res = robot.rotate('L')
    #     self.assertEquals(res, (Direction.WEST, [0, 0]))
    def testMoveRotate(self):
        robot = Robot()
        res = robot.move()
        res = robot.rotate('R')
        res = robot.move()
        self.assertEquals(res, (Direction.EAST, [1, 1]))

unittest.main()


'''
> M
Robot at (0, 1) facing North  
> L
Robot at (0, 1) facing West
> M
Robot at (-1, 1) facing West
> M
Robot at (-2, 1) facing West
> R
Robot at (-2, 1) facing North
> R
Robot at (-2, 1) facing East
> M
Robot at (-1, 1) facing East
> ?
Command the robot with:
  L - turn left
  R - turn right
  M - move forward
  ? - this message
  Q - quit
> Q
Robot shutting down.
'''