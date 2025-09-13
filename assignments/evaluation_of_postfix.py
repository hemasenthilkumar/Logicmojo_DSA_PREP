class Solution:
    from typing import List
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t.strip("+-").isdigit():
                stack.append(int(t))
            elif t == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif t == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif t == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))  # --> truncates towards 0
        return stack[-1]