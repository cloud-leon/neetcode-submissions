class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', '}':'{' , ']':'['}


        stack = []
        for ch in s:
            if stack and ch in pairs.keys():
                if stack[-1] == pairs[ch]:
                    stack.pop()
                    continue
            stack.append(ch)
        return len(stack) == 0