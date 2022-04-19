'''
Students may decide to take different "tracks" or sequences of courses in the Computer Science curriculum. 
There may be more than one track that includes the same course, but each student follows a single linear track from a "root" node to a "leaf" node. 
In the graph below, their path always moves left to right.

Write a function that takes a list of (source, destination) pairs, 
and returns the name of all of the courses that the students could be taking when they are halfway through their track of courses.

Sample input:
all_courses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]

Sample output (in any order):
    ["Data Structures", "Creative Writing", "Databases", "Intro to Computer Science"]

All paths through the curriculum (midpoint *highlighted*):

*Intro to C.S.* -> Graphics
Intro to C.S. -> *Data Structures* -> Algorithms -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> COBOL
Intro to C.S. -> *Data Structures* -> Logic -> Compiler
Creative Writing -> *Databases* -> System Administration
*Creative Writing* -> System Administration
Creative Writing -> *Data Structures* -> Algorithms -> COBOL
Creative Writing -> *Data Structures* -> Logic -> COBOL
Creative Writing -> *Data Structures* -> Logic -> Compilers

Visual representation:

                    ____________
                    |          |
                    | Graphics |
               ---->|__________|
               |                          ______________
____________   |                          |            |
|          |   |    ______________     -->| Algorithms |--\     _____________
| Intro to |   |    |            |    /   |____________|   \    |           |
| C.S.     |---+    | Data       |   /                      >-->| COBOL     |
|__________|    \   | Structures |--+     ______________   /    |___________|
                 >->|____________|   \    |            |  /
____________    /                     \-->| Logic      |-+      _____________
|          |   /    ______________        |____________|  \     |           |
| Creative |  /     |            |                         \--->| Compilers |
| Writing  |-+----->| Databases  |                              |___________|
|__________|  \     |____________|-\     _________________________
               \                    \    |                       |
                \--------------------+-->| System Administration |
                                         |_______________________|

Complexity analysis variables:

n: number of pairs in the input
'''

import collections
from inspect import currentframe
allCourses = [
    ["Logic", "COBOL"],
    ["Data Structures", "Algorithms"],
    ["Creative Writing", "Data Structures"],
    ["Algorithms", "COBOL"],
    ["Intro to Computer Science", "Data Structures"],
    ["Logic", "Compilers"],
    ["Data Structures", "Logic"],
    ["Creative Writing", "System Administration"],
    ["Databases", "System Administration"],
    ["Creative Writing", "Databases"],
    ["Intro to Computer Science", "Graphics"],
]


def dfs(graph, src, dst, cur, paths):
    if cur[-1] == dst:
        paths.append(list(cur))
        return 
    for nxt in list(graph[cur[-1]]):
        dfs(graph, src, dst, cur + [nxt], paths)

def findAllPaths(allCourses, src, dst):
    #Form graph
    graph = collections.defaultdict(set)
    for c1, c2 in allCourses:
        graph[c1].add(c2)

    #Find all paths from src to dst
    paths = []
    dfs(graph, src, dst, [src], paths)
    return paths 

src = "Creative Writing" 
dst = "COBOL"
paths = findAllPaths(allCourses, src, dst)
print(paths)


src = "Creative Writing" 
dst = "System Administration"
paths = findAllPaths(allCourses, src, dst)
print(paths)