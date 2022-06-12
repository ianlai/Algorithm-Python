'''
vim('hello', 'llhrx') => 'hxllo'
vim('hello', 'hhhhhhrx') => 'xello'
vim('hello', 'llhrx') => 'hxllo'
vim ('hello', 'flrx;ry') => 'hexyo'
vim('heeellloooooll','hhl4lflrx;ry') => 'heeellxoooooyl'


l: move the cursor right   //4l 代表往右走4步
h: move the cursor left
rx: replace the character under the cursor with x //replace with x
fl: 按 ; 继续向右找。按 "," 沿反方向找到下一个 "l"      //right find l
Fl: 按 ; 继续向左找。按 "," 沿反方向找到下一个 "l"      //left find l

'''
from ast import Raise


class VimOperator(object):
    """Mock vim action for a string"""
    def __init__(self, _input ,action):
        self.input = list(_input)
        self.action = action
        self._init_metric()
        self.process()

    def _init_metric(self):
        self.index = 0
        self.left_limit = 0
        self.right_limit = len(self.input)-1
        self.find_action = 'f'
        self.find_target = ''

    def process(self):
        """
        1. number : judge by isnumeric() function. next item will be 'l' or 'h'
        2. 'l'    : move cursor left 1 time
        3. 'h'    : move cursor right 1 time
        4. 'r'    : next item will be a char value, replace current index elem with next char
        5. 'f'    : next item will be a char value, find the next char value from cursor(to right)
        6. 'F'    : ....................................................................(to left)
        7. ';'    : a ';' will follow a 'f'/'F' action , find the same element follow the action
        8. ','    : a ','.................................................................reverse action
        """
        idx = 0  #action's index
        while idx < len(self.action):
            ch = self.action[idx]
            print("ch:", ch, self.index)
            # case 1 : for number
            if ch.isdigit():
                for _ in range(int(ch)):
                    self.move(self.action[idx+1])
                idx += 2
            # case 2 : for left / right
            elif ch in ('l','h'):
                self.move(ch)
                idx += 1
            # case 3 : replace value
            elif ch == 'r':
                self.input[self.index] = self.action[idx+1]
                idx += 2
            # case 4 : find
            elif ch in ('f', 'F'):
                target = self.action[idx+1]
                self.find(ch, target)
                idx += 2
            
            # case 5 : followed find
            elif ch in (';', ','):
                if ch == ";": 
                    self.find(self.find_action, self.find_target)
                    idx += 1
                else: 
                    self.find_action = 'F' if self.find_action == 'f' else 'f'
                    self.find(self.find_action, self.find_target)
                    idx += 1
            else:
                print("Error")


    def move(self, direction):
            """ :param direction
                  h means moving cursor to left
                  l means moving cursor ro right
             """
            if direction == 'h':
                  self.index = max(self.left_limit, self.index-1)
            else:
                  self.index = min(self.right_limit, self.index+1)

    def find(self, op, target):
        originalInputIdx = self.index
        self.find_action = op
        self.find_target = target
        if op == 'f':
            while self.index < len(self.input) and self.input[self.index] != target:
                self.index += 1
            if self.index == len(self.input):
                self.index = originalInputIdx
        else:
            while self.index >= 0 and self.input[self.index] != target:
                self.index -= 1
            if self.input == -1: 
                self.index = originalInputIdx

    def get_output(self):
            return "".join(self.input)

import unittest
class Test(unittest.TestCase):
    def test_replace(self):
        s = VimOperator('hello','llhrx')
        self.assertEquals(s.get_output(),'hxllo')

    def test_move_replace(self):
        s = VimOperator('hello','2h3lrx')
        self.assertEquals(s.get_output(),'helxo')

    def test_find_found(self):
        s = VimOperator('hellobabc','fbrx')
        self.assertEquals(s.get_output(),'helloxabc')
    
    def test_find_no_found(self):
        s = VimOperator('hellobabc','fmrx')
        self.assertEquals(s.get_output(),'xellobabc')  #back to 0

    def test_find_repeating(self):
        s = VimOperator('hellobabc','fbhhrq;lrw')
        self.assertEquals(s.get_output(),'helqobwbc') 
    
    def test_find_reverting(self):
        s = VimOperator('hellobacdstbc','fb3lru,lrwhhrx')
        self.assertEquals(s.get_output(),'hellxbwcustbc') 

if __name__ == '__main__':
    unittest.main()
    # s = VimOperator('hello','2h3lrx')  #helxo
    # s.process()
    # print(s.get_output())

    # s = VimOperator('hellobabc','fbrx')  #found b: helloxabc
    # s.process()
    # print(s.get_output())

    # s = VimOperator('hellobabc','fmrx')  #not found m: xellobabc (back to 0)
    # s.process()
    # print(s.get_output())