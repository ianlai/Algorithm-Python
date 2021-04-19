#!/usr/local/bin/python3
from os import listdir
from os import walk
import re

path        = 'algo'
fileList    = []
dirList     = []
filtered    = []
def appendFiles(path, dirList, fileList):
    for (dirpath, dirnames, filenames) in walk(path):
        fileList.extend(filenames)
        dirList.extend(dirnames)
        break

def filteredFiles(path, dirList, fileList, filtered):
    appendFiles(path, dirList, fileList)
    # print("File List:", fileList)
    # print("Dir List :", dirList)
    
    for d in dirList:
        appendFiles(path+"/"+d, [], fileList)

    for f in fileList:
        found = re.search("_{2}\d+_{2}.+\.py", f)
        if found:
            filtered.append(found.string)

def getPracticeNumber():
    return len(filtered)

def showQuizListFromDir():
    filteredFiles(path, dirList, fileList, filtered)
    filtered.sort()

    print()
    print("=====================================")
    print("============= Local Repo ============")
    print("=====================================")
    for e in filtered:
        print(e)
    print("=====================================")
    print("Num of Python Practice: ", getPracticeNumber())
    print()

# run as a script (not module)
if __name__ == '__main__':
    showQuizListFromDir()


