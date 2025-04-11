class Solution:
    def isValid(self, s: str) -> bool:
        parenthese = { '(':')','{':'}','[':']'}

        stack = []

        for bracket in s:
            if bracket in parenthese:
                stack.append(bracket)
            else:
                if not stack or parenthese[stack.pop()] != bracket:
                    return False
        return not stack
