class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            elif ch == '{':
                stack.append('}')
            else:
                if len(stack)==0 or stack.pop()!=ch:
                    return False
        return not stack           

        