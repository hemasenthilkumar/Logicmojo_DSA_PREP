
class Solution:
    def preToInfix(self, pre_exp):
        # Code here
        stack = []
        for token in reversed(pre_exp):
            if token.isalnum():
                stack.append(token)
            else:
                first = stack.pop()
                second = stack.pop()
                stack.append(f"({first}{token}{second})")
        
        return stack[-1]