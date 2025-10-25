class Solution:
    def isValid(self, s: str) -> bool:
        closed_brackets = {']': '[', ')': '(', '}': '{'}
        bracket_stack = []
        for value in s:
            if open_bracket:= closed_brackets.get(value, None):
                bracket = bracket_stack.pop() if bracket_stack else None
                if open_bracket != bracket:
                    return False
            else:
                bracket_stack.append(value)

        return not bracket_stack