'''
======================================
[Problem-1] 給定一個學生ID list，求裡面兩兩一組的共同課程。

You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. 
The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.

Sample Input:

student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

Sample Output (pseudocode, in any order):

find_pairs(student_course_pairs_1) =>
{
  [58, 17]: ["Software Design", "Linear Algebra"]
  [58, 94]: ["Economics"]
  [58, 25]: ["Economics"]
  [94, 25]: ["Economics"]
  [17, 94]: []
  [17, 25]: []
}

Additional test cases:

Sample Input:

student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

Sample output:

find_pairs(student_course_pairs_2) =>
{
  [0, 42]: []
  [0, 9]: []
  [9, 42]: []
}

'''
import collections

student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

def findPairs(courses):
    idToCourses = collections.defaultdict(set)
    for id, course in courses:
        idToCourses[id].add(course)
    print(idToCourses)

    idPairToCourses = {}
    ids = list(idToCourses.keys())
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            idPair = (ids[i], ids[j])
            commonCourses = []
            for course in idToCourses[ids[i]]:
                if course in idToCourses[ids[j]]:
                    commonCourses.append(course)
            idPairToCourses[idPair] = commonCourses
    return idPairToCourses

res = findPairs(student_course_pairs_1)
for pair in res.keys():
    print(pair, "->", res[pair])


'''
======================================
[Problem-2] 

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


#這是DAG 不用考慮繞圈的問題。
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

    print("graph:", graph)

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