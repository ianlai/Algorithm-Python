'''
You are a developer for a university. Your current project is to develop a system for students to find courses they share with friends. 
The university has a system for querying courses students are enrolled in, returned as a list of (ID, course) pairs.
Write a function that takes in a list of (student ID number, course name) pairs and returns, for every pair of students, a list of all courses they share.

給定一個學生ID list，求裡面兩兩一組的共同課程。

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