class Solution(object):
    def isValid(self, s: str) -> bool:
        """
            Check for valid parenthesis
            Conditions to meet
            An input string is valid if:
            1. Open brackets must be closed by the same type of brackets.
            2. Open brackets must be closed in the correct order.
            3. Every close bracket has a corresponding open bracket of the same type.
        """
        stack = []
        matching_parenthesis = {")":"(",
                                "]":"[",
                                "}":"{",}
        for char in s:
            if char in matching_parenthesis.keys():
                stack.append(char)
            elif char in matching_parenthesis.values():
                if len(stack) == 0 or stack.pop() != matching_parenthesis[char]:
                    return False
            else:
                return True
                