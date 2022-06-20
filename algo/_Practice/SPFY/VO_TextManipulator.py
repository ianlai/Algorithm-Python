'''
Text Manipulator

Hello World
Input: hhlhllhlhhll
Output: Hello World
               _
               2 
Input: rhllllllrw
Output: hello world
                    _
                    6

Input: rh 6l 9l 4h rw
Output: hello world
                    _
                    6
Input: 9l rL 7h 2rL
Output: HeLLo WorLd     //replace 1 -> no cursor move ; replace 2 -> cursor moved by 1 
                   _
                   3
Input: 999999999999999999999999999lr0
Output: Hello Worl0    //stay before last char 
                             _
                            10
Input: 999rs
Output: sssssssssss
                               _
                              10
===================================

input:
  - target (string)
  - command (string) 
output: 
  - output (string)  
  - position (int)
'''
class TextManipulator:
    def __init__(self, target = "Hello World", command = ""):
        self.cursor = 0
        self.target = list(target)
        self.command = command 
        self.commandIdx = 0

    def process(self):
        # commandIdx = 0 
        commandNumString = ""
        while self.commandIdx < len(self.command):
            cmd = self.command[self.commandIdx]
            #self.runSingleCommand(cmd)
            if cmd.isdigit():  
                commandNumString += cmd
                self.commandIdx  += 1
            else: 
                if commandNumString != "": #repeating cmd 
                    #print("repeating: ", commandNumString, "x", cmd)
                    for _ in range(int(commandNumString)):
                        self.runSingleCommand(cmd)
                    commandNumString = ""
                else:                      #single cmd
                    self.runSingleCommand(cmd)
                
                if cmd in ('h', 'l'): 
                    self.commandIdx += 1
                else:
                    self.commandIdx += 2
            print("cmd:", cmd)
            self.generateOutput()

    def runSingleCommand(self, cmd):
        #print("run", cmd)
        if cmd in ('h', 'l'): #move right, left
            if cmd == 'h' and self.cursor > 0:
                self.cursor -= 1
            elif cmd == 'l' and self.cursor < len(self.target) - 1: #len - 1
                self.cursor += 1
            #self.commandIdx  += 1
        elif cmd == 'r':      #replace
            self.target[self.cursor] = self.command[self.commandIdx + 1]
            #self.commandIdx  += 2
            
    def generateOutput(self):
        print("".join(self.target), self.cursor)

#textManipulator = TextManipulator("Hello World", "rhllllllrw")
#textManipulator = TextManipulator("Hello World", "rh6l9l4hrw")
textManipulator = TextManipulator("Hello World", "123lr0")
textManipulator.process()
textManipulator.generateOutput()


