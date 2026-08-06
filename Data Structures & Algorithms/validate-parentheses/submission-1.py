class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"}":"{",
            "]":"[",
            ")":"("}  
        stack = []

        for c in s:
            if c not in dic.keys():
                stack.append(c)
            else:
                if stack and dic[c] == stack[-1]:
                    stack.pop()
                else:
                    return False


        return True if len(stack)== 0 else False