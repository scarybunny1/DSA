class Solution:
    def simplifyPath(self, path: str) -> str:
        
        p = path.split('/')
        stack = []
        for directory in p:
            if len(directory) == 0:
                continue
            elif directory == "..":
                if stack:
                    stack.pop()
            elif directory == ".":
                continue
            else:
                stack.append(directory)
        return "/" + "/".join(stack)