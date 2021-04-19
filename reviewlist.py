#!/usr/local/bin/python3
from os import listdir
from os import walk
import re

path        = 'review'
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
        found = re.search("_{1}\d+_{1}.+\.py", f)
        if found:
            filtered.append(found.string)

def getReviewNumber():
    #If we don't call the showQuiz in the main program, we need to do this
    filteredFiles(path, dirList, fileList, filtered) 
    return len(filtered)

def showQuizListFromDir():
    filteredFiles(path, dirList, fileList, filtered)
    filtered.sort()

    print()
    print("=====================================")
    print("=============== Review ==============")
    print("=====================================")
    for e in filtered:
        print(e)
    print("=====================================")
    print("Num of Review: ", getReviewNumber())
    print()

# run as a script (not module)
if __name__ == '__main__':
    #print(getReviewNumber())
    showQuizListFromDir()


