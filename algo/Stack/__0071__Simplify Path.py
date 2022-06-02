class Solution:
    '''
    /a/b/../c        -> ["a", "b", "..", "c"] -> /a/c
    /a/b/..//.//../c -> ["a", "b", "..", "", ".", "", "..", "c"] -> /c
    '''
    # 2022/06/02
    # Stack [O(N): 68% / O(N): 98%]
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split('/')
        stack = []
        for folder in pathArr:
            if folder == "." or folder == "":
                continue
            elif folder == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(folder)
        return "/" + "/".join(stack)