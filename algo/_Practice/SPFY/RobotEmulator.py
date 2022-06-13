'''
二维坐标系 机器人初始化在(0,0)面朝北 输入L 90度左转 R 90度右转， M就前进, Q终止游戏  
每次输入指令就返回类似 "Robot is at (1,3) facing North" 这种
'''
from enum import Enum, IntEnum

class Direction(IntEnum):
    NORTH = 1
    EAST  = 2
    SOUTH = 3
    WEST  = 4

class Robot:
    directionToStep = {
        Direction.NORTH: (-1, 0), 
        Direction.EAST : ( 0, 1), 
        Direction.SOUTH: ( 1, 0), 
        Direction.WEST : ( 0,-1)
    }
    def __init__(self):
        self.direction = Direction.NORTH
        self.location = [0, 0]

    def process(self):
        cmdArr = []
        while True:
            cmd = input("Input operation: ")
            if cmd == "Q":
                self.runCommands(cmdArr)
                break
            else:
                cmdArr.append(cmd)
        print(self.location, self.direction)

    def runCommands(self, cmdArr):
        print(cmdArr)
        for cmd in cmdArr:
            print(">>>>>", cmd)
            if cmd in ('L', 'R'):
                if cmd == 'R':
                    self.direction += 1
                    if self.direction > 4:
                        self.direction = Direction.NORTH
                else:
                    self.direction -= 1
                    if self.direction == 0:
                        self.direction = Direction.WEST
            elif cmd == 'M':
                self.location[0] += Robot.directionToStep[self.direction][0]
                self.location[1] += Robot.directionToStep[self.direction][1]
            else:
                print("Error")
            #print("###", self.location, self.direction)
        return self.location, self.direction

import unittest
class Test(unittest.TestCase):
    def test_runCommands1(self):
        robot = Robot()
        self.assertEquals(robot.runCommands(['M', 'M', 'L', 'M']), ([-2, -1], Direction.WEST)) 
    def test_runCommands2(self):
        robot = Robot()
        self.assertEquals(robot.runCommands(['M', 'M', 'L', 'M', 'R', 'M', 'M']), ([-4, -1], Direction.NORTH)) 

unittest.main()

#robot = Robot()
#robot.runCommands(['M', 'M', 'L', 'M'])    