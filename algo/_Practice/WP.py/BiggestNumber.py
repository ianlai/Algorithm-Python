"""
  LANGUAGE:
  Python3

  PROBLEM:
  Biggest Number

  DESCRIPTION:
  Given an array of numbers, arrange them in a way that yields the largest value.

  INSTRUCTIONS:
  1) Implement the biggest_number method
  2) Add appropriate tests to verify the accuracy of your solution

  EXAMPLES:
  [95, 132, 554, 12] = 9555413212
  [2, 15, 3, 88, 1, 12, 225, 513] = 885133225215121
  
  [95, 922, 554, 12] = 9555413212
  
  95922
  92295 
  
"""
import functools

def biggest_number(numbers):
    def comp(x, y):
        if x + y < y + x:
            return 1
        return -1
    
    numbersString = [str(x) for x in numbers]
    numbersString.sort(key = functools.cmp_to_key(comp))
    
    res = ""
    for numStr in numbersString:
        res += numStr
    return int(res)

class Test:
    def __init__(self, input, output):
        self.input = input
        self.output = output

def run_tests():
    tests = [
        Test([95, 132, 554, 12], 9555413212),
        Test([2, 15, 3, 88, 1, 12, 225, 513], 885133225215121),
        Test([95, 9, 991], 999195),
        Test([11, 113], 11311)

    ]

    return all((biggest_number(test.input) == test.output) for test in tests)

if run_tests():
    print("Tests passed")
else:
    print("Tests failed")
