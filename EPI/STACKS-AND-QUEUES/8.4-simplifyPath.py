class Solution:
    def simplifyPath(self, path: str) -> str:

        newPath = (token for token in path.split("/") if token not in [".", ""])
        stack = []

        for segment in newPath:
            if segment == "..":
                if stack: 
                    stack.pop()
            else:
                stack.append(segment)

        return "/" + "/".join(stack)